# coding=utf-8

# '''
# Given an array of integers and an integer k, find
#  out whether there are two distinct indices i and
#  j in the array such that nums[i] = nums[j] and
#  the difference between i and j is at most k.
# '''

# 需要一直更新temp内的value

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = {}
        value = float('inf')
        for s in xrange(len(nums)):
            if temp.has_key(nums[s]):
                # 这个if考虑 [1,0,1,1] 1的参数输入
                if s - temp[nums[s]] < value: value = s - temp[nums[s]]
            temp[nums[s]] = s   # 不管有没有这个key都需要重新赋值给key

        return value <= k
