# coding=utf-8

'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''

'''
总结backtracking就是各种条件下的控制，通过for循环起始变量
和递归函数调用参数的来实现, Beat 68.93%
'''

class Solution(object):
    def CS(self, st, ed, lst, tmp, base, step, limit):
        """
        st和ed表示对k的控制，base和limit表示n的控制
        step来表示不超过10的限制
        """
        if st == ed:
            if base == limit:
                ref = tmp[:]
                lst.append(ref)
            return

        for i in xrange(step+1, 10):
            tmp.append(i)
            self.CS(st + 1, ed, lst, tmp, base + i, i, limit)
            tmp.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        self.CS(0, k, res, tmp, 0, 0, n)
        return res
