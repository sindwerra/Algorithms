# coding=utf-8

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

'''
算是双指针的套路题了吧，只要注意循环的边界在哪里就好
Beat 86.36%
公司：Facebook
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        st, ed = 0, n - 1
        while st <= ed - 2:
            if nums[st] == nums[st + 1] and nums[st + 1] == nums[st + 2]:
                del nums[st + 2]
                ed -= 1
                n -= 1
            else:
                st += 1
        return n
