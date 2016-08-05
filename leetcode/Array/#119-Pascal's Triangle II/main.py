# coding=utf-8

# 还可以尝试更快的方法，这个方法是参照一改的，有非常多不必要的运算

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        temp1 = []
        temp2 = []
        for s in xrange(rowIndex + 1):
            temp1 = []
            if s == 0:
                temp1.append(1)
            elif s == 1:
                temp1.extend([1, 1])
                temp2.extend([1, 1])
            else:
                for a in xrange(s + 1):
                    if a == 0 or a == s: temp1.append(1)
                    else: temp1.append(temp2[a - 1] + temp2[a])
                temp2 = []
                temp2.extend(temp1)

        return temp1
