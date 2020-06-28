# coding=utf-8

'''
Given an array S of n integers, are there elements a, b, c, and d in S
such that a + b + c + d = target? Find all unique quadruplets in the array
which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

'''
最直接的做法就是把3sum的代码再在外面套一层，注意第二个点检查重复的条件就行
但是速度不快，Beat 17.32%
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ori = 0
        res = []

        while ori <= n - 4:
            a = nums[ori]
            if ori > 0 and nums[ori] == nums[ori - 1]:
                ori += 1
                continue
            base = ori + 1
            while base <= n - 3:
                b = nums[base]
                if base > ori + 1 and nums[base] == nums[base - 1]:
                    base += 1
                    continue
                st, ed = base + 1, n - 1
                while st <= ed - 1:
                    c, d = nums[st], nums[ed]

                    if a + b + c + d == target:
                        res.append([a, b, c, d])
                        while ed > st and nums[ed] == nums[ed - 1]:
                            ed -= 1
                        while ed > st and nums[st] == nums[st + 1]:
                            st += 1
                        ed -= 1
                    elif a + b + c + d > target:
                        ed -= 1
                    else:
                        st += 1
                base += 1
            ori += 1
        return res
