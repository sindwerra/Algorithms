# coding=utf-8

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

'''
根据geeksforgeeks的原则,会产生尾0的数只有既包含了2还有5的因数的数，
且一对2和5产生一个0
但是所有数出现的2因子数量肯定要多过5的因子数量，所以只要计算有多少个5就行
且五的次幂处还会有一个额外的5产生，整个过程相当于
result = function(n/5) + function(n/25) + function(n/125)...
Beat 62.40%
公司：Bloomberg
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        divider = 5
        while n / divider:
            tmp = n / divider
            res += tmp
            divider *= 5
        return res
