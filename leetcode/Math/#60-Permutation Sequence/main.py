# coding=utf-8

'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

'''
根据回溯法就可以发现全排列的一定规律，当只要取其中一组数时其实就变成了一个数学问题
Beat 47.39%
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lst = range(1, n + 1)
        number = 1
        k -= 1
        for s in range(1, n):
            number *= s

        count = 0
        while k > 0:
            tup = divmod(k, number)
            for s in range(tup[0] + count, count, -1):
                lst[s], lst[s - 1] = lst[s - 1], lst[s]
            k = tup[1]
            number /= (n - 1 - count)
            count += 1

        res = ''
        for a in lst:
            res += str(a)
        return res
