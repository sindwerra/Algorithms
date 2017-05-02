'''
最简洁鲁棒的代码
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