# coding=utf-8

# 主要熟悉下dict的函数

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = {}
        for s in nums:
            if temp.has_key(s): return True
            temp[s] = 1

        return False
