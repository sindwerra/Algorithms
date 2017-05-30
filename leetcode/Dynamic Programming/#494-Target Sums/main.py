# coding=utf-8

'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + 
and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

'''
gitbook已经详细说了
Beat 8.59%
公司：Google， Facebook
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        up = sum(nums)
        down = -up
        if S < down or S > up:
            return 0
        
        
        dp = [([0] * (up - down + 1)) for _ in xrange(n + 1)]
        for i in xrange(up - down + 1):
            if i + down == nums[0]:
                dp[1][i] += 1
            if i + down == -nums[0]:
                dp[1][i] += 1
        
        for i in xrange(2, n + 1):
            for j in xrange(up - down + 1):
                a, b = 0, 0
                if j + nums[i - 1] < up - down + 1:
                    a = dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    b = dp[i - 1][j - nums[i - 1]]
                dp[i][j] = a + b

        return dp[n][S - down]