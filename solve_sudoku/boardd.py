from __future__ import annotations
import copy
from cell import Cell
from typing import Literal, Type, Union
from colorama import Fore, Back, Style
from candidates import Candidates

class Boardcheckpoint():


    def __init__(self, board:list[Cell], empty_cells:list[Cell], cell_i_tried:Cell, attempts:list[int]):
        self.board = copy.deepcopy(board)
        self.empty_cells = copy.deepcopy(empty_cells)
        self.cell_i_tried = cell_i_tried
        self.attempts = attempts
        self.try_again = False
    







SOLVED = "SOLVED"
NOT_SOLVED = "NOT_SOLVED"

var = (
    "..71........2.3.5...........3....8....4........867..3.6..42...1.723....4..1.8.6.5"
)
def makeboard(board_str:str) -> list[Cell]:
    sudokubräde:list[Cell] = []
    for i in range(81):
        letter = board_str[i]
        r = int(i / 9)
        c = i - (r * 9)

        cb = int(c / 3)
        rb = int(r / 3)
        block = rb * 3 + cb

        cell = Cell(r, c, block, parsecellvalue(letter), Candidates(list(range(1,10))))

        sudokubräde.append(cell)
    return sudokubräde

def parsecellvalue(char:str) -> int:
    match char:
        case "9":
            return 9
        case "8":
            return 8
        case "7":
            return 7
        case "6":
            return 6
        case "5":
            return 5
        case "4":
            return 4
        case "3":
            return 3
        case "2":
            return 2
        case "1":
            return 1
        case ".":
            return 0
    raise ValueError(f"I am not expecting somethign like: {char}")

def make_board2(board:list[Cell], empty_cells:list[Cell], cell_i_tried:Cell) -> Boardcheckpoint:
    s_board = Boardcheckpoint(board, empty_cells, cell_i_tried, [])

    return s_board

def print_board(board:list[Cell]):
    for i in range(81):
        if not i % 9:
            print() 
        v = board[i].value
        print("." if v == 0 else v , end=' ')

def empty_cell_row(empty_cell:Cell, board:list[Cell]) -> list[int]:
    row_values:list[int] = []
    for i in range(len(board)):
        cell = board[i]
        if cell.row == empty_cell.row and cell.value != 0:
            invalid_cell = cell.value
            row_values.append(invalid_cell)
    return row_values


def empty_cell_col(empty_cell:Cell, board:list[Cell]) -> list[int]:
    col_values = []
    for i in range(len(board)):
        cell = board[i]
        if cell.col == empty_cell.col and cell.value != 0:
            invalid_cell = cell.value
            col_values.append(invalid_cell)
    return col_values


def empty_cell_block(empty_cell:Cell, board:list[Cell]) -> list[int]:
    block_values = []
    for i in range(len(board)):
        cell = board[i]
        if cell.block == empty_cell.block and cell.value != 0:
            invalid_cell = cell.value
            block_values.append(invalid_cell)
    return block_values


def find_candidates(empty_cell:Cell, board:list[Cell]):

    col_values = empty_cell_col(empty_cell, board)
    row_values = empty_cell_row(empty_cell, board)
    block_values = empty_cell_block(empty_cell, board)

    candidates = empty_cell.candidates.candidates
    candidates = list(
        filter(lambda candidate: candidate  not in col_values, candidates)
        )

    candidates = list(
        filter(lambda candidate: candidate  not in row_values, candidates)
        )

    candidates = list(
        filter(lambda candidate: candidate  not in block_values, candidates)
    )

    return candidates


def find_empty_cell(board:list[Cell]) -> Union[Cell, bool]:
    for i in range(len(board)):
        cell = board[i]
        if cell.value == 0:
                return cell
    else: 
        return True


def find_all_empty_cells(board:list[Cell]) -> list[Cell]:
    empty_cells:list[Cell] = []
    for i in range(len(board)):
        cell = board[i]
        if cell.value == 0:
            empty_cells.append(cell)
    return empty_cells

def print_solution(solution:Union[list[Cell], str]):
    if type(solution) == list[Cell]:
        color_board(solution)
    else:
        print(solution)



def fetch_cells(board:list[Cell]) -> list[Cell]:
    empty_cells = find_all_empty_cells(board)
    for empty_cell in empty_cells:
            empty_cell.candidates.candidates = find_candidates(empty_cell, board)        
    return empty_cells

def find_lowest_number_of_candidates(empty_cells:list[Cell]) -> Cell:
    low_candidate = []
    for cell in empty_cells:
        low_candidate.append(len(cell.candidates.candidates))
    small_num = min(low_candidate)
    for cell in empty_cells:
        if len(cell.candidates.candidates) == small_num:
            return cell
    
    raise ValueError("something bad happened")



def color_board(board:list[Cell]):
    dict_of_cells = get_all_candidates_for_empty_cells(board)
    if dict_of_cells == None:
        print_board(board)
        return


    color = ''
    for i in range(81):
        if not i % 9:
            print() 
        v = board[i].value
        item = board[i]
        if item in dict_of_cells:  
            match len(dict_of_cells[item]): 
                case 0:
                    color = Back.RED
                case 1:
                    color = Back.YELLOW
                case 2:
                    color = Back.BLUE
                case 3:
                    color = Back.GREEN
                case _:
                    color = Back.RESET
        
        print(color + "." + Back.RESET if v == 0 else v , end=' ')



def get_all_candidates_for_empty_cells(board:list[Cell]) -> dict[Cell, list[int]]:
    empty_cells = find_all_empty_cells(board)
    empty_cell_dictionary = {}
    if len(board) == 0:
        raise ValueError("woopsie doopsie")
    for empty_cell in empty_cells:
        candidates = find_candidates(empty_cell, board)
        empty_cell_dictionary[empty_cell]= candidates
    return empty_cell_dictionary


def are_candidates_valid(empty_cells:list[Cell]) -> bool:
    for empty_cell in empty_cells:
        if len(empty_cell.candidates.candidates) == 0:
            return False     
    return True