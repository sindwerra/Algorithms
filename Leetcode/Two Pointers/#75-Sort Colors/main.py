# coding=utf-8

'''
Given an array with n objects colored red, white or blue, sort them so
that objects of the same color are adjacent, with the colors in the
order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then
overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

# 荷兰国旗问题，三指针解决，0往前换推指针，1只往前推指针，2往后换指针不动
# Beat 59.05%

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        st, ed = 0, len(nums) - 1
        cur = 0
        while cur <= ed:
            if nums[cur] == 0:
                nums[cur], nums[st] = nums[st], nums[cur]
                st += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[ed] = nums[ed], nums[cur]
                ed -= 1
            else:
                cur += 1
