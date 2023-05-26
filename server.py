from flask import Flask, request, render_template, session
import sys, os

sys.path.append(os.getcwd() + "/solve_sudoku")
from sudoku_solver import solve_board
from boardd import makeboard, create_string_for_board_output
from import_requests import fetch_board


app = Flask(__name__)
app.config['SECRET_KEY']='yeah aod, yeah'



@app.route("/")
def hello_world():
    return render_template("homepage!.html")


@app.route("/see-board")
def show_board():
    board_str = fetch_board()
    board = makeboard(board_str)
    output = create_string_for_board_output(board)
    session['my_var'] = board_str

    return (
        f"""
        <p>you can reload the page if you want to see a new board.<br><br></p> 
    <form action="/solve">
    <p>{output}<style>p{{font-family: monospace;}}</style></p><br>
    <input type="submit" value="Solve the board">
</form><br>"""
    )


@app.route("/solve")
def solve():
    board = session.get('my_var', None)
    erm = makeboard(board)
    hehe = solve_board(erm)
    yeah = create_string_for_board_output(hehe)
    return f"""
    <p> Here is your solved board :)<br><br></p>
    
    <p>{yeah}<style>p{{font-family: monospace;}}</style></p><br>"""
