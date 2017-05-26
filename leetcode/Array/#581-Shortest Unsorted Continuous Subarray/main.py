# coding=utf-8

'''
Given an integer array, you need to find one continuous subarray that 
if you only sort this subarray in ascending order, then the whole array 
will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make 
the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

'''
太愚蠢了.. 这个题想了太久对撞指针的做法，但是因为有相等的数所以实际上是行不通的
其实只要排序完数组再拿来和原数组比对第一个不同的点和最后一个不同的点就知道结果了
Beat 86.08%
公司：liveramp，Google
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(nums)
        n = len(nums)
        
        left, right = 0, n - 1

        while left < n:
            if nums[left] != tmp[left]:
                break
            left += 1
        
        while right:
            if nums[right] != tmp[right]:
                break
            right -= 1
        
        return right - left + 1 if right >= left else 0