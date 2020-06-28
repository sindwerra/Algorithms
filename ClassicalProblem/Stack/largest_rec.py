# coding=utf-8

'''
Given n non-negative integers representing the histogram's bar height where the 
width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

'''
一道思维很不好理解的栈的题目，具体逻辑太复杂，简单讲就是维护一个单调上升的栈单调上升的趋势一旦
随遍历打破则将栈中元素倒出直到重新满足单调性为止，通过此过程往复求得最大面积(具体看九章)
Beat 88.44%
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        stack = [0]
        n = len(heights)
        result = heights[0]

        # 全遍历过程

        for i in xrange(1, n):
            if heights[i] <= heights[stack[-1]]:
                while stack and heights[stack[-1]] >= heights[i]:
                    tmp = stack.pop()
                    if stack:
                        result = max(result, heights[tmp] * (i - stack[-1] - 1))
                    else:
                        result = max(result, heights[tmp] * i)
            stack.append(i)
        
        # 收尾过程

        while stack:
            tmp = stack.pop()
            if stack:
                result = max(result, heights[tmp] * (n - 1 - stack[-1]))
            else:
                result = max(result, heights[tmp] * n)
            
        return result
        