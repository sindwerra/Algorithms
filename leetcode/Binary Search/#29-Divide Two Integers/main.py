# coding=utf-8

'''
Divide two integers without using multiplication,
division and mod operator.

If it is overflow, return MAX_INT.
'''

'''
主要根据就是每次递归是O(lgn)时间复杂度，且调用递归的次数必定是常数级别的
如果不能用除法二分就只能用 >> 符号了
另外每次必须把二分后的余数都收集起来直到这个余数不足以除一次dividor
上限是2**31 - 1，下线是-2**31，两个都是负数则用~符号反转bit再加一
Beat 86.52%
'''

class Solution(object):
    def helper(self, dividend, divisor):
        if dividend - divisor >= divisor:
            a = self.helper(dividend >> 1, divisor)
            rem = dividend - (dividend >> 1) - (dividend >> 1)
            return [a[0] + a[0], rem + a[1] + a[1]]
        elif dividend >= divisor:
            return [1, dividend - divisor]
        else:
            return [0, dividend]

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor: return sys.maxint
        if not dividend: return 0

        a = abs(dividend)
        b = abs(divisor)
        tmp = self.helper(a, b)
        res = tmp[0]

        while tmp[1] >= b:
            tmp = self.helper(tmp[1], b)
            res += tmp[0]

        if dividend > 0 and divisor > 0:
            return min(res, sys.maxint - 1)
        elif dividend < 0 and divisor < 0:
            return min(res, sys.maxint - 1)
        else:
            return max(~res + 1, -sys.maxint)
