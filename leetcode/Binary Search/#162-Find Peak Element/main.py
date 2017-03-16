# coding=utf-8

'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak
element and return its index.

The array may contain multiple peaks, in that case return the index
to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your
function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.
'''

# 其实不是对数时间复杂度，只做到O(n/3)的时间复杂度
# 总的来说确保每一次跳步的位置之前一位肯定比当前位置小就好
# Beat 88.11%

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [-sys.maxint - 1] + nums + [-sys.maxint - 1]  # 左右添加两个dummy
        i = 1
        while i <= n:
            if nums[i + 1] > nums[i]:              # 相邻的数大于当前值
                if nums[i + 2] > nums[i + 1]:      # i，i+1， i+2的值是上升序列
                    i += 2
                else: return i                     # i+1大于i+2 且 i小于i+1，返回
            else:
                return i - 1                       # 返回当前值

        # i跳到n时右边值必然小于nums[n],所以跳出循环的值只有可能是n-1
        # 意味着在循环内没有结果的情况下只有可能是最后一个数了

        return i - 2
