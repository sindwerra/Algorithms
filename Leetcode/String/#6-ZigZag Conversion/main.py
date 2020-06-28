# coding=utf-8

'''
这题要注意一开始numRows的大小问题，另外就是非边界行的规律
Beat 82.20%
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        result = ''
        step = 2 * numRows - 2
        n = len(s)
        
        if n <= numRows or numRows <= 1:
            return s

        for i in xrange(numRows):
            start = i
            if start == 0 or start == numRows - 1:
                while start < n:
                    result += s[start]
                    start += step
            else:
                offset = start
                while start < n:
                    if start >= numRows and (start - offset * 2) < n:
                        result += s[start - offset * 2]
                    result += s[start]
                    start += step

                if start - offset * 2 < n:
                    result += s[start - offset * 2]
        
        return result