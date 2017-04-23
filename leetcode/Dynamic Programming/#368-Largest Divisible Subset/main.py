# coding=utf-8

'''
Given a set of distinct positive integers, find the largest subset such that 
every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or 
Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''

'''
排好序后的数组只要每一个当前数能整除之前数组最后一个数则整个数组的所有数
都可以整除不用逐个检查了
Beat 84.39%
公司：Google
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        
        if not n:
            return []
        
        res = [[] for _ in xrange(n)]
        res[0] = [nums[0]]

        for i in xrange(1, n):
            q = 1
            index = None
            res[i].append(nums[i])
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if q < len(res[j]) + 1:
                        q = len(res[j]) + 1
                        index = j
            if index is not None:
                res[i].extend(res[index])
        
        length = 1
        result = res[0]
        for lst in res:
            count = len(lst)
            if count > length:
                length = count
                result = lst
        return result