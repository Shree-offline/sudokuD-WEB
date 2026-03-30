from flask import Flask, render_template, jsonify, request
import random
import os

app = Flask(__name__)

def generate_sudoku():
    # A base grid. In a full game, you'd use a library to generate millions of unique boards.
    base_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    # Let's shuffle the first 3 rows just so the "New Game" button visibly does something!
    block = base_grid[0:3]
    random.shuffle(block)
    base_grid[0:3] = block
    
    return base_grid

# 1. Loads the main page
@app.route('/')
def index():
    grid = generate_sudoku()
    return render_template('index.html', grid=grid)

# 2. API for JavaScript to request a new board
@app.route('/new_game', methods=['GET'])
def new_game():
    new_grid = generate_sudoku()
    return jsonify({"grid": new_grid}) # Sends data back as JSON

# 3. API for JavaScript to send the user's answers to Python
@app.route('/check_solution', methods=['POST'])
def check_solution():
    data = request.json
    user_grid = data.get('grid')
    
    # A very basic check: see if there are any 0s (empty spaces) left
    is_full = True
    for row in user_grid:
        if 0 in row or "" in row:
            is_full = False
            break
            
    if is_full:
        return jsonify({"message": "Board is full! Great job!"})
    else:
        return jsonify({"message": "Keep going! There are still empty spaces."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
