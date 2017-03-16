# coding=utf-8

'''
Given an array S of n integers, are there elements a, b, c
in S such that a + b + c = 0? Find all unique triplets in
the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
此题不能用双固定指针一个游动指针，这样会错过一些情况，参考一个神test case
[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
这个case包含了多重重复元素，还有易错过情况
最后因为有超大数组的存在，为了不超时必须想办法避免重复数组答案
（直接检测是不行的）
首先用单固定指针，然后在固定指针范围的右侧设置左右两个活动指针来找到所有结果
Beat 2.74%
(这道题不可能更快了，除非用特殊方法来超过O(n^2)的时间复杂度，之前的代码很多都超时了)
用for loop也不行
公司：Amazon, Microsoft, Bloomberg, Facebook, Adobe, Works Applications
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums) - 1
        base = 0
        res = []
        while base <= n - 2:
            a = nums[base]
            st = base + 1
            end = n
            if base > 0 and nums[base] == nums[base - 1]:
                base += 1
                continue
            while st <= end - 1:
                b, c = nums[st], nums[end]
                if a + b + c == 0:
                    res.append([a, b, c])
                    while nums[end] == nums[end - 1] and end > st:
                        end -= 1
                    while nums[st] == nums[st + 1] and end > st:
                        st += 1
                    end -= 1
                elif a + b + c < 0:
                    st += 1
                else:
                    end -= 1
            base += 1
        return res
