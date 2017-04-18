# coding=utf-8

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

'''
根据九章的算法的做的题，写出一个findKthNumber的函数就可以解决这个问题
Beat 95.03%
公司：Google, Zenefits, Microsoft, Apple, Yahoo, Dropbox, Adobe
'''

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n, m = len(A), len(B)
        if (n + m) % 2:
            return self.findKthNumber(A, 0, B, 0, (n + m) / 2 + 1)
        else:
            return (self.findKthNumber(A, 0, B, 0, (n + m) / 2) + self.findKthNumber(A, 0, B, 0, (n + m) / 2 + 1)) / 2.0

    def findKthNumber(self, A, startIndexA, B, startIndexB, k):
        if startIndexA >= len(A):
            return B[startIndexB + k - 1]
        if startIndexB >= len(B):
            return A[startIndexA + k - 1]
        
        if k == 1:
            return min(A[startIndexA], B[startIndexB])
        
        # 当下标长度不够时，直接将比较值视为正无穷，再砍掉较小的数组k/2个数就行（仔细想想为什么可以这样）

        A_key = A[startIndexA + k / 2 - 1] if startIndexA + k / 2 - 1 < len(A) else sys.maxint 
        B_key = B[startIndexB + k / 2 - 1] if startIndexB + k / 2 - 1 < len(B) else sys.maxint

        if A_key < B_key:
            return self.findKthNumber(A, startIndexA + k / 2, B, startIndexB, k - k / 2)
        else:
            return self.findKthNumber(A, startIndexA, B, startIndexB + k / 2, k - k / 2)