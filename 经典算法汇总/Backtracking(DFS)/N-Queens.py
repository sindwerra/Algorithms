'''
N皇后经典问题
'''

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        tmp, res = [], []
        self.helper(0, n, tmp, res)
        return res
    
    def helper(self, count, limit, tmp, res):
        if count == limit:
            ref = tmp[:]
            res.append(self.drawBoard(tmp, limit))
            return 
        
        for i in xrange(limit):
            if not self.isValid(i, count, tmp):
                continue
            tmp.append(i)
            self.helper(count + 1, limit, tmp, res)
            tmp.pop()
    
    def isValid(self, curCol, curRow, tmp):
        for row, col in enumerate(tmp):
            if col == curCol:
                return False
            if row - col == curRow - curCol:
                return False
            if row + col == curRow + curCol:
                return False
        return True    
    
    def drawBoard(self, location, n):
        res = []
        for row in xrange(n):
            string = ''
            for col in xrange(n):
                if location[row] != col:
                    string += '.'
                else:
                    string += 'Q'
            res.append(string)
        
        return res
