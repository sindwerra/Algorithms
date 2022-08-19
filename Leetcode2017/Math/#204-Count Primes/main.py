# coding=utf-8

'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''

'''
按照提示做的，首先用O(n)空间的桶，其次只需要遍历到n^0.5的数就行
再次每一个遍历的数都是从自己的平方开始再逐个加倍就行
最后桶里面0的个数就是结果
Beat 67.58%
公司：Amazon, Microsoft
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = [0] * (n + 1)
        st = 2
        while st * st <= n:
            if tmp[st]:
                st += 1
                continue
            cur = st * st
            while cur <= n:
                tmp[cur] = 1
                cur += st
            st += 1

        return tmp[2:n].count(0)
