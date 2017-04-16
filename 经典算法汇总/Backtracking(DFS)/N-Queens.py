'''
N皇后经典问题,用循环检测对角线攻击的方法
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


'''
第二种，用set检查对角线攻击的问题
Beat 83.33%
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col, l_dia, r_dia = set([]), set([]), set([])
        tmp, res = [], []
        self.helper(n, tmp, res, col, l_dia, r_dia, 0)
        return res

    def helper(self, end, tmp, res, col, l_dia, r_dia, count):
        if count >= end:
            res.append(self.drawBoard(tmp, end))
            return 
        
        for i in xrange(end):
            if not self.valid(count, i, col, l_dia, r_dia):
                continue
            tmp.append(i)
            col.add(i)
            l_dia.add(count - i)
            r_dia.add(count + i)
            self.helper(end, tmp, res, col, l_dia, r_dia, count + 1)
            tmp.pop()
            col.remove(i)
            l_dia.remove(count - i)
            r_dia.remove(count + i)
    
    def valid(self, i, j, col, l_dia, r_dia):
        if j in col:
            return False
        if (i - j) in l_dia:
            return False
        if (i + j) in r_dia:
            return False
        return True

    def drawBoard(self, location, n):
        res = []
        for i in xrange(n):
            string = ''
            for j in xrange(n):
                if location[i] == j:
                    string += 'Q'
                else:
                    string += '.'
            res.append(string)
        
        return res