'''
最简洁鲁棒的代码，没有重复的数字
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        st, end = 0, n - 1
        while st < end:
            mid = st + (end - st) / 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                st = mid + 1
        return nums[st]


class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo] 

'''
有重复数字的版本
'''

class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid if nums[hi] != nums[mid] else hi - 1
        return nums[lo]