from flask import Flask, request

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
    

    return args["sudoku"]
