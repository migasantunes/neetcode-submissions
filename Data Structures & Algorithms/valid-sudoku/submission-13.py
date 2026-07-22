class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUnique(row): return False

        for col in range(9):
            if not self.isUnique([board[row][col] for row in range(9)]): return False 

        for rowOffset in range(3):
            for colOffset in range(3):
                if not self.isUnique([board[row + rowOffset*3][col + colOffset*3] for row in range(3) for col in range(3)]): return False
        
        return True
    
    def isUnique(self, listNum: List[str]) -> bool:
        count = 10 - listNum.count(".")
        if (len(set(listNum)) != count): return False
        return True