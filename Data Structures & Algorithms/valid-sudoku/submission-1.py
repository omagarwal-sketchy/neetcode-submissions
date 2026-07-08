class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums=[]
        for i in board:
            for j in i:
                if j!=".":
                    nums.append(j)   
            if len(set(nums))!=len(nums):
                return False
            nums=[]
        nums=[]
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i]!=".":
                    nums.append(board[j][i])
            if len(set(nums))!=len(nums):
                return False
            nums=[]
        nums=[]
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(0,3):
                    for j in range(0,3):
                        if board[r+i][c+j]!=".":
                            nums.append(board[r+i][c+j])
                if len(set(nums))!=len(nums):
                    return False
                nums=[]                     
        return True