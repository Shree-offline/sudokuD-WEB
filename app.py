from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

def generate_sudoku():
    # A simple starting grid for your Neon Punch theme
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
    return base_grid

@app.route('/')
def index():
    grid = generate_sudoku()
    return render_template('index.html', grid=grid)

if __name__ == '__main__':
    # This part ensures it runs on Render or locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
