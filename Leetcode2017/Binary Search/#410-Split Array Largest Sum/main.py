# coding=utf-8

'''
Given an array which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

'''
就是复印书的题换了更原始的说法
Beat 64.08%
公司：Baidu, Facebook
'''

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        st, ed = max(nums), sum(nums)
        while st + 1 < ed:
            mid = st + (ed - st) / 2
            if self.check(nums, mid) <= m:
                ed = mid
            else:
                st = mid

        if self.check(nums, st) <= m:
            return st
        return ed

    def check(self, nums, count):
        tmp = 0
        result = 1

        for num in nums:
            tmp += num
            if tmp > count:
                result += 1
                tmp = num
        
        return result