# coding=utf-8

'''
Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 
0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''

'''
这里是DP做法，不过这题DP过不了，只能用贪心
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dis = [0] * n

        for i in xrange(1, n):
            q = i + 1
            for j in xrange(i):
                if nums[j] + j >= i:
                    q = min(q, dis[j] + 1)
            dis[i] = q
        
        return dis[n - 1]