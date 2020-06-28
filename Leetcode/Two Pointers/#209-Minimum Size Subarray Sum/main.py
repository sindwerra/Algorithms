# coding=utf-8

'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log n).
'''

# 双指针的题，不过boundary case很多，Beat 89.23%

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s: return 0
        res = len(nums)
        n = res
        if res == 1: return 1 if nums[0] >= s else 0
        tmp = nums[0]
        st, ed = 0, 0
        while ed <= n - 1:
            if tmp < s:
                ed += 1
                if ed <= n - 1:
                    tmp += nums[ed]
            else:
                if ed - st + 1 < res:
                    res = ed - st + 1
                tmp -= nums[st]
                st += 1
        return res

'''
用九章强化班的标准双指针模板重新做的
看起来是双重循环，实际上两个指针都是只向前运动的，所以还是O(n)
Beat 78.08%
公司：Facebook
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        length = sys.maxint

        j = 0
        tmp = 0

        for i in xrange(n):
            while j < n and tmp < s:
                tmp += nums[j]
                j += 1

            if j - i < length and tmp >= s:
                length = j - i

            tmp -= nums[i]

        return length if length != sys.maxint else 0
