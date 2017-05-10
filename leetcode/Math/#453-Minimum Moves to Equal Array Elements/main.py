# coding=utf-8

'''
Given a non-empty integer array of size n, find the minimum number of moves 
required to make all array elements equal, where a move is incrementing 
n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

'''
纯数学，智商碾压... 除最大外全加一和最大减一效果一样
公司：Indeed, Coursera
'''

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmp_num = min(nums)
        result = 0

        for num in nums:
            result += (num - cmp_num)
        return result