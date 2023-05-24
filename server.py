from flask import Flask, request, render_template
import sys, os

sys.path.append(os.getcwd() + "/solve_sudoku")
from sudoku_solver import solve_board
from boardd import makeboard, create_string_for_board_output


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("homepage!.html")


@app.route("/see-board")
def show_board():
    args = request.args
    board = makeboard(args["sudoku"])
    output = create_string_for_board_output(board)
    return (output,"""style="font-family:monospace" """,
        """
    <form action="/solve">
    <input type="submit" value="Solve the board">
</form><br>"""
    )


@app.route("/solve")
def solve():
    args=request.args
    board = makeboard(args["sudoku"])
    hehe = solve_board(board)
    yeah = create_string_for_board_output(hehe)
    return yeah
