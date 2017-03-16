# coding=utf-8

'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i
is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

# 还是双指针，从两端逐渐靠近就行，每次只移动高度低的那块板子
# Beat 82.16%

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        st, ed = 0, len(height) - 1
        res = 0
        while st < ed:
            if height[st] < height[ed]:
                res = max(res, height[st] * (ed - st))
                st += 1
            else:
                res = max(res, height[ed] * (ed - st))
                ed -= 1
        return res     
