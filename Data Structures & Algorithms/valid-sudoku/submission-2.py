class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use set for duplicates
        # this is a 9 by 9 question
        
        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False
        
        # check columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False
        
        # check each small square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for row in range (i, i +3):
                    for col in range(j, j+3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] not in seen:
                            seen.add(board[row][col])
                        else:
                            return False
        
        return True