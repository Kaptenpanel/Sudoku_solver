#ysstdtyftyf



from boardd import makeboard, create_string_for_board_output
from sudoku_solver import solve_board

board = makeboard("........1.5...89...42...3.85...3.1.2..8.25.........45..19...27....7.2....8.....13")

mmm = solve_board(board)

string = create_string_for_board_output(mmm)

print(string)