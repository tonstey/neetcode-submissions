class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                square = squares[(j // 3) + (i // 3) * 3] 
                row = rows[i]
                col = cols[j]

                if board[i][j] != "." and (board[i][j] in square or board[i][j] in row or board[i][j] in col):
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    square.add(board[i][j])
                    row.add(board[i][j])
                    col.add(board[i][j])
            print(squares)

        return True