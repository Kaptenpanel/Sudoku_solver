from flask import Flask, request, render_template, session
import sys, os

sys.path.append(os.getcwd() + "/solve_sudoku")
from sudoku_solver import solve_board
from boardd import makeboard, create_string_for_board_output


app = Flask(__name__)
app.config['SECRET_KEY']='yeah aod, yeah'



@app.route("/")
def hello_world():
    return render_template("homepage!.html")


@app.route("/see-board")
def show_board():
    args = request.args
    board_str = args["sudoku"].replace(" ", "")
    board = makeboard(board_str)
    output = create_string_for_board_output(board)
    session['my_var'] = board_str
    return (
        f"""
    <form action="/solve">
    <p>{output}<style>p{{font-family: monospace;}}</style></p><br>
    <input type="submit" value="Solve the board">
    <p>Now I can go home :) </p> <br>
    <input type="text"
</form><br>"""
    )


@app.route("/solve")
def solve():
    board = session.get('my_var', None)
    erm = makeboard(board)
    hehe = solve_board(erm)
    yeah = create_string_for_board_output(hehe)
    return f"""<p>{yeah}<style>p{{font-family: monospace;}}</style></p><br>"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
