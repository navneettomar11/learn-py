from typing import  List

def surrounded_region(board: List[List[str]]) -> None:
    row = len(board)

    for i in range(1, row-1):
        cols = len(board[row])
          
