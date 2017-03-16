# coding=utf-8

'''
Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

'''
现在大致能想通这题“贪心”在哪里了，但是最优子结构还是看不出来，只知道O(N)的解法
O(n^2)不知道
Beat 89.59%
公司：Microsoft
'''

'''
做法：从头开始遍历，只要能触到数组重点就算True
每一个落脚点如果能跳步数不是0则将此值加上当前落脚点基准往前跳，直到落脚点值是0为止
如果是0则往回逐个遍历，直到找到一个点的值加点坐标可以跳过刚才为0的点为止
找不到就返回False
'''

class Solution(object):
    def canJump(self, A):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st, ed = 0, len(A) - 1
        if not A[0] and ed:
            return False
        while st < ed:
            if not A[st]:
                tmp = st - 1
                while tmp and A[tmp] + tmp <= st:
                    tmp -= 1
                if A[tmp] + tmp > st:
                    st = A[tmp] + tmp
                elif A[tmp] + tmp == ed:
                    return True
                else:
                    return False
            else:
                st += A[st]
        return True
