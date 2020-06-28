# coding=utf-8

'''
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

# 思路非常隐蔽的一道题，和一般的动归区别很大
# 因为存在0和负数会导致积翻转或是归零的情况，所以必须维护两个变量curMax和curMin
# 来计算当前点的最大积，一个深刻的教训...

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        curMax, curMin = 1, 1
        for s in nums:
            tmp1 = max(curMax * s, s, curMin * s)
            tmp2 = min(curMax * s, s, curMin * s)
            curMax = tmp1
            curMin = tmp2
            res.append(tmp1)
        return max(res)
