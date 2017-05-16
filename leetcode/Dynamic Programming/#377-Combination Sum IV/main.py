# coding=utf-8

'''
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''

'''
不知道这种算是坐标性动态规划还是接龙型，其实非常简单，利用target建一个数组然后
逐个递增推至target这个数就能知道答案了，当然nums列表必须要排序
Beat 78.36%
公司：Google, Snapchat, Facebook
'''

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        result = [0] * (target + 1)
        result[0] = 1

        for i in xrange(target + 1):
            for num in nums:
                if i < num:
                    break
                result[i] += result[i - num]
        
        return result[target]