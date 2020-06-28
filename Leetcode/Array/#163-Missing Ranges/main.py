# coding=utf-8

'''
Given a sorted integer array where the range of elements are in the
inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
return ["2", "4->49", "51->74", "76->99"].
'''

'''
注意好upper lower的逻辑就好，没有什么复杂算法，纯粹考虑各种情况就行
Beat 90.78%
公司：Google
'''

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]
        res = []
        if nums[0] > lower:
            if lower == nums[0]:
                pass
            elif lower != nums[0] - 1:
                res.append(str(lower) + '->' + str(nums[0] - 1))
            else:
                res.append(str(lower))

        for s in range(1, len(nums)):
            if nums[s] == nums[s - 1] or nums[s] - 1 == nums[s - 1]:
                continue
            if nums[s] - 1 == nums[s - 1] + 1:
                res.append(str(nums[s] - 1))
            else:
                res.append(str(nums[s - 1] + 1) + '->' + str(nums[s] - 1))

        if nums[-1] < upper:
            if upper == nums[-1]:
                pass
            elif upper - 1 != nums[-1]:
                res.append(str(nums[-1] + 1) + '->' + str(upper))
            else:
                res.append(str(upper))
        return res
