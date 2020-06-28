# coding=utf-8

'''
Given an integer array of size n, find all elements that appear more than
⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
Do you have a better hint? Suggest it!
'''

'''
实质还是Moore's voter algorithm的改进， 这次需要两个index和两个count
并且是还需要算法的第二部分来检查整个结果是否正确
Beat 51.13%
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        mj1_index, mj2_index = 0, 0
        count1, count2 = 0, 0
        base = 0
        n = len(nums)
        for s in range(n):
            if nums[s] == nums[mj1_index]:
                count1 += 1
            else:
                if not base:
                    mj2_index = s
                    count2 = 1
                    base += 1
                elif nums[mj2_index] == nums[s]:
                    count2 += 1
                elif count1 < 0:             # count1只有在count小于0时才要更改
                    mj1_index = s
                    count1 = 1
                else:
                    count1 -= 1
                    count2 -= 1
                    if not count2:
                        mj2_index = s
                        count2 = 1

        count1, count2 = 0, 0
        res = []
        for s in nums:
            if nums[mj1_index] == s:
                count1 += 1
            if nums[mj2_index] == s:
                count2 += 1
        if count1 > n / 3:
            res.append(nums[mj1_index])
        if count2 > n / 3 and nums[mj1_index] != nums[mj2_index]:
            res.append(nums[mj2_index])

        return res
