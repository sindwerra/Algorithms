# coding=utf-8

'''
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

# 写的是array标签，其实是双指针来做
# Beat 78.63%

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        st, ed = 0, 1
        n = len(nums) - 1
        if n == 0: return [str(nums[0])]   # 一个数的list
        if n == -1: return []              # 空list
        res = []
        while ed <= n:
            if nums[ed] - nums[ed - 1] == 1:
                ed += 1
            else:
                if st == ed - 1: res.append(str(nums[st]))
                else:
                    res.append(str(nums[st]) + '->' + str(nums[ed - 1]))
                st = ed
                ed += 1

        # 这里用来收最后一次的数

        if st == ed - 1:
            res.append(str(nums[st]))
        else:
            res.append(str(nums[st]) + '->' + str(nums[ed - 1]))

        return res
