# coding=utf-8

'''
Given an array nums and a target value k, find the maximum length
of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the
32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and
is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is
the longest)

Follow Up:
Can you do it in O(n) time?
'''

'''
根据lintcode上一个相对简单的题来的思路，简而言之就是重新列一个数组
从头翻卷所有下标之前的元素的和，最后通过各下标和之差可以得到这些子数组的和
然后通过store这个dict记录位置，最后找到最长的符合要求的子数组
这个方法有点慢
Beat 23.31%
公司：Palantir, Facebook
'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        tmp = [0] * n
        tmp[0] = nums[0]
        for s in range(1, n):
            tmp[s] = tmp[s - 1] + nums[s]
        store = {}
        dis = 0
        for s in range(n):
            if tmp[s] == k:
                rg = s + 1
                if rg > dis:
                    dis = rg
            if store.has_key(tmp[s] - k):
                rg = s - store[tmp[s] - k][0]
                if rg > dis:
                    dis = rg
            if store.has_key(tmp[s]):
                store[tmp[s]].append(s)
            else:
                store[tmp[s]] = [s]

        return dis
