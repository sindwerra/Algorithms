# coding=utf-8

'''
Given a non-empty integer array, find the minimum number of moves required to make 
all array elements equal, where a move is incrementing a selected element by 1 or 
decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''

'''
和一的思路很像，关键在于想到和一差不多类似的基准值，在一里是最大值
在这里是中位数
Beat 73.41%
'''

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        median = self.quickSel(nums, 0, n - 1, (n + 1) / 2)
        
        result = 0
        for num in nums:
            result += abs(num - median)
        
        return result

    def quickSel(self, nums, start, end, k):
        if start >= end:
            return nums[end]
        
        left, right = start, end
        pivot = nums[left + (right - left) / 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if start + k - 1 <= right:
            return self.quickSel(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quickSel(nums, left, end, k - (left - start))
        
        return nums[right + 1]
