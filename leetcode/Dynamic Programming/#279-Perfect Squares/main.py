# coding=utf-8

'''
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

'''
就是动归做，但是要注意检查的上限是当前数的根号就行了
Beat 63.05%
公司：Google
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        for i in xrange(1, n + 1):
            q = i
            for j in xrange(1, int(i ** 0.5) + 1):
                q = min(q, 1 + res[i - j * j])
            res[i] = q
        return res[n]


'''
下面是纯数学方法，还没搞懂是怎么回事
Beat 96.59%
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in xrange(n+1):
            temp = i * i
            if temp <= n:
                if int((n - temp)** 0.5 ) ** 2 + temp == n: 
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3