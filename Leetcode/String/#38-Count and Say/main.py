# coding=utf-8

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

'''
暴力就可以做，难道有什么其他思路？
Beat 62.23%
公司：Facebook
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = 1
        res = str(tmp)
        for s in xrange(n - 1):
            tmp = str(tmp)
            res = ''
            count = 1
            for i in range(len(tmp) - 1):
                if tmp[i] == tmp[i + 1]:
                    count += 1
                else:
                    res += (str(count) + str(tmp[i]))
                    count = 1
            res += (str(count) + str(tmp[-1]))
            tmp = int(res)
        return res
