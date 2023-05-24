from flask import Flask, request
import sys, os
sys.path.append(os.getcwd() + '/solve_sudoku') 
from sudoku_solver import solve_board
from boardd import makeboard, create_string_for_board_output


app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
<form action="/solve">
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
    erm = makeboard(args["sudoku"])
    hehe = solve_board(erm)
    yeah = create_string_for_board_output(hehe)
    return yeah
