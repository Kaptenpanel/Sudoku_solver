
from __future__ import annotations
from candidates import Candidates


class Cell:
    '''this is a cell in the sudoku board'''
    def __init__(
        self, row: int, col: int, block: int, value: int, candidates: Candidates
    ):
        self.row = row
        self.col = col
        self.block = block
        self.value = value
        self.candidates = candidates

    def __repr__(self) -> str:
        return (
            "("
            + "r:"
            + str(self.row)
            + ","
            + "c:"
            + str(self.col)
            + ","
            + "b:"
            + str(self.block)
            + ","
            + "v:"
            + str(self.value)
            + ","
            + ":"
            + str(self.candidates.candidates)
            + ")"
        )

    def compare(self, other: Cell) -> bool:
        if (
            self.row == other.row
            and self.col == other.col
            and self.block == other.block
        ):
            return True
        return False
