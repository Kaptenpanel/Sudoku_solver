from cell import Cell
from boardd import (
    Boardcheckpoint,
    make_board2,
    fetch_cells,
    find_lowest_number_of_candidates,
    are_candidates_valid,
)


def solve_board(board: list[Cell]):
    saved_boards: list[Boardcheckpoint] = []
    for _ in range(10000000):
        empty_cells = fetch_cells(board)
        if len(empty_cells) == 0:
            return board
        if are_candidates_valid(empty_cells) == False:
            if len(saved_boards) == 0:
                return "THE SUDOKU BOARD CANNOT BE SOLVED"
            else:
                board = saved_boards[-1].board
                saved_boards[-1].try_again = True
                empty_cells = fetch_cells(board)
        good_cell = find_lowest_number_of_candidates(empty_cells)
        if len(good_cell.candidates.candidates) == 1:
            good_cell.value = good_cell.candidates.candidates[0]
        elif len(good_cell.candidates.candidates) == 0:
            saved_boards.pop(-1)
            continue
        else:
            if len(saved_boards) != 0:
                if (saved_boards[-1].try_again) == True:
                    for attempt in saved_boards[-1].attempts:
                        if attempt in good_cell.candidates.candidates:
                            good_cell.candidates.candidates.remove(attempt)
                    good_cell.value = good_cell.candidates.candidates[0]
                    saved_boards[-1].try_again = False
                    continue
            saved_board = make_board2(board, empty_cells, good_cell)
            good_cell.value = good_cell.candidates.candidates[0]
            saved_board.attempts.append(good_cell.value)
            saved_boards.append(saved_board)


if __name__ == "__main__":
    original = "..71........2.3.5...........3....8....4........867..3.6..42...1.723....4..1.8.6.5"

    hard_case = "........1.5...89...42...3.85...3.1.2..8.25.........45..19...27....7.2....8.....13"

    hard_case2 = ".....8......5...9...5.397.2.1.945.............2.7.....7.......9..3.2..474.....21."

    almost_unsolvable = "..64..7..2....1.9.....8.....1..2..8.7.......4..3...5.......3..6..57.....9......2."

    unsolvable = "2..9............6......1...5.26..4.7.....41......98.23.....3.8...5.1......7......"
