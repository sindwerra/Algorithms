# coding=utf-8

'''
Given an unsorted array of integers, find the length of
longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore
the length is 4. Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

# 一道非常经典的动态规划问题，思路不多说，这种题要背的
# Beat 37.23%,好像在找值部分可以用二分搜索提高速度

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = [0] * n
        for s in xrange(n):
            q = 0
            for k in xrange(s):
                if nums[k] < nums[s]:
                    q = max(q, res[k])
            res[s] += (q + 1)
        return max(res) if n <> 0 else 0
