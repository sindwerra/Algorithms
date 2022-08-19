# coding=utf-8

'''
A sequence of number is called arithmetic if it consists of at
least three elements and if the difference between any two consecutive
elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.
A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular,
this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4]
and [1, 2, 3, 4] itself.
'''

'''
看不太出这是个动态规划，总之每到一点只要跟后面一个点数值相同就开始往回数，只要有连续
两个或两个以上的相同数值就可以算
Beat 98.46%
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        tmp = [0] * n
        for i in range(1, n):
            tmp[i] = A[i] - A[i - 1]
        res = 0
        for s in range(1, n - 1):
            if tmp[s] == tmp[s + 1]:
                st = s + 1
                cur = st
                while cur >= 2 and tmp[cur] == tmp[cur - 1]:
                    res += (st - s)
                    cur -= 1
        return res
