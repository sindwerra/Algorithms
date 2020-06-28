# coding=utf-8

'''
Given scores of N athletes, find their relative ranks and the people with the top three 
highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got 
"Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''

'''
哈希表表权重即可
Beat 86.83%
公司：Google
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        jisho = {}
        tmp = sorted(nums, reverse=True)
        
        for num in nums:
            jisho[num] = 0
        
        for index, num in enumerate(tmp):
            jisho[num] = str(index + 1)
            if index == 0:
                jisho[num] = 'Gold Medal'
            if index == 1:
                jisho[num] = 'Silver Medal'
            if index == 2:
                jisho[num] = 'Bronze Medal'
        
        res = []
        for num in nums:
            res.append(jisho[num])
        
        return res