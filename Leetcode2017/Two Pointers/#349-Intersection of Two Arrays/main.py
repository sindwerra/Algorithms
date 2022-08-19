# coding=utf-8

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

'''
这里用双指针的做法做的
Beat 85.17%
'''

class Solution(object):
    def intersection(self, nums1, nums2):
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
                while one < n and nums1[one] == a:
                    one += 1
                while two < m and nums2[two] == a:
                    two += 1
            elif nums1[one] < nums2[two]:
                one += 1
            else:
                two += 1
        
        return res