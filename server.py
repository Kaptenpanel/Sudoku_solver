from flask import Flask, request

from solve_sudoku.boardd import color_board, makeboard
from solve_sudoku.sudoku_solver import solve_board

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """<form action="/solve">
    <label for="sudoku">put your sudoku string here:</label>
  <input type="text" id="sudoku" name="sudoku"><br><br>
  <input type="submit" value="Submit">
</form>"""



@app.route("/see-board")
def show_board():
    return """
    
    """


@app.route("/solve")
def solve():
    args = request.args
    board = makeboard(args["sudoku"])
    solution = solve_board(board)
    result = color_board(solution)

    return result
