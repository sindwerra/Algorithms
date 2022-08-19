# coding=utf-8

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element 
from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
'''

'''
Heap的题基本都得有个哈希表查重才行
Beat 87.50%
公司：Google, Uber
'''

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        res = []
        heap = []
        store = {}
        n, m = len(nums1), len(nums2)
        if not n or not m:
            return []
        heapq.heappush(heap, [nums1[0] + nums2[0], (0, 0)])

        for i in xrange(k):
            if not heap:
                return res
            number, location = heapq.heappop(heap)
            left, right = location[0], location[1]
            res.append([nums1[location[0]], nums2[location[1]]])
            if left + 1 < n and not store.has_key((left + 1, right)):
                heapq.heappush(heap, [nums1[left + 1] + nums2[right], (left + 1, right)])
                store[(left + 1, right)] = 1
            if right + 1 < m and not store.has_key((left, right + 1)):
                heapq.heappush(heap, [nums1[left] + nums2[right + 1], (left, right + 1)])
                store[(left, right + 1)] = 1
        return res
        