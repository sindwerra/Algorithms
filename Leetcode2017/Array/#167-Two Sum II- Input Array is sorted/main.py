# coding=utf-8

'''
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such
that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2)
are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

# 标准双指针，都没想到会这么快
# Beat 96.05%

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        st, ed = 0, len(numbers) - 1
        while st < ed:
            if numbers[ed] + numbers[st] > target:
                ed -= 1
            elif numbers[ed] + numbers[st] < target:
                st += 1
            else:
                return [st+1, ed+1]
        return None
