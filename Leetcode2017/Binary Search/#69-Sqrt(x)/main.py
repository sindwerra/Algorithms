# coding=utf-8

'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''

'''
二分法做，不过有内置判断的其他逻辑，Beat 35.88% 有点慢
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        st, ed = 0, x
        while st < ed:
            mid = (st + ed) / 2
            if mid * mid < x:
                st = mid + 1
                if st * st > x: return st - 1
                if st * st == x: return st
            elif mid * mid > x:
                ed = mid - 1
                if ed * ed <= x: return ed
            else:
                return mid
        return st
