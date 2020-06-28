# coding=utf-8

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that 
you cannot load all elements into the memory at once?
'''

'''
第一题的方法就是最优解了
Beat 88.45%
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        n, m = len(nums1), len(nums2)

        one, two = 0, 0
        res = []
        
        while one < n and two < m:
            if nums1[one] == nums2[two]:
                a = nums1[one]
                res.append(a)
                one += 1
                two += 1
            elif nums1[one] < nums2[two]:
                one += 1
            else:
                two += 1
        
        return res
                