# coding=utf-8

'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume
the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

# 如果没有without extra space这个条件就应该用计数排序做最合适
# 因为题目有要求空间复杂度O（1）时间复杂度O（n），则根据数组特征，两遍遍历之后除了
# 重复的数其他数必定归位了（有待证明这个结论），这时再用第三遍遍历找index和值不一样的数即可
# Beat 41.09% （只有四组test case，正确性有待商榷）

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for asfd in xrange(2):
            for s in xrange(n):
                if nums[s] != s + 1:
                    nums[nums[s] - 1], nums[s] = nums[s], nums[nums[s] - 1]
        for index in xrange(n):
            if index + 1 != nums[index]:
                res.append(index + 1)
        return res
