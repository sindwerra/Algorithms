# coding=utf-8

'''
Given n non-negative integers representing an elevation map where the width of each 
bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

'''
这个属于对向指针的题，两根代表木桶边框的指针每次都选择矮的那块往对向走直到找到中间一块隔板跟开始
那块一样高或者更高或者直接就碰到另外一个指针，遍历过程中每一步加上初始隔板高与当前高度的差就是能装
水的量
Beat 85.49%
公司：Google, Twitter, Zenefits, Amazon, Apple, Bloomberg
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        st, ed = 0, n - 1

        while st < n and height[st] == 0:
            st += 1
        while ed >= 0 and height[ed] == 0:
            ed -= 1
        
        result = 0

        while st < ed:
            if height[st] < height[ed]:
                cur = height[st]
                st += 1
                while st < ed and cur > height[st]:
                    result += (cur - height[st])
                    st += 1
            else:
                cur = height[ed]
                ed -= 1
                while st < ed and cur > height[ed]:
                    result += (cur - height[ed])
                    ed -= 1
        
        return result