from flask import Flask, request
import sys, os
sys.path.append(os.getcwd() + '/solve_sudoku') 
from solve_sudoku.sudoku_solver import solve_board
from solve_sudoku.boardd import makeboard


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
    makeboard('78921689471290471289739018301')
    solve_board

    return args["sudoku"]
