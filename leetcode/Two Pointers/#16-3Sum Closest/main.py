# coding=utf-8

'''
Given an array S of n integers, find three integers in S such that the
sum is closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

'''
3Sum问题的改进版，此题关于重复的避免只需要在外层的固定指针处即可
因为当内循环的a+b+c等于target时，函数返回结果而不会继续搜索
另外需要cmp和res两个变量一个记录最小差值，一个记录当前a+b+c的值
Beat 92.18%
公司：Bloomberg
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        start = 0
        cmp, res = sys.maxint, 0
        while start <= n - 3:
            a = nums[start]
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue
            st, ed = start + 1, n - 1
            while st <= ed - 1:
                b, c = nums[st], nums[ed]
                if abs(a + b + c - target) < cmp:
                    cmp = abs(a + b + c - target)
                    res = a + b + c
                if a + b + c == target:
                    return target
                elif a + b + c < target:
                    st += 1
                else:
                    ed -= 1
            start += 1
        return res
