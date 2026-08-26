class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows: in each list, no duplicate
        for i in range(len(board)):
            count = []
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in count:
                    count.append(board[i][j])
                else:
                    return False
        
        # check column: for the same index postion, no dupicate
        for i in range(len(board)):
            count = []
            for j in range (len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in count:
                    count.append(board[j][i])
                else:
                    return False
        
        # now check 3 * 3
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                count = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] not in count:
                            count.append(board[row][col])
                        else:
                            return False
        
        return True
