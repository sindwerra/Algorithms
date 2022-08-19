# coding=utf-8

'''
Given an unsorted array of integers, find the length of the longest 
consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

'''
这道题就是用union find的标准做法来做的，不过貌似是不能用数组来做parent集合了
这里用的dict来做，因此也导致速度上比较慢
Beat 10.77%
公司：Google, Facebook
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        parent = {}

        for num in nums:
            parent[num] = [num, 1]
        

        result = [1]
        for node, val in parent.items():
            if node + 1 in parent:
                self.union(node, node + 1, parent, result)
            if node - 1 in parent:
                self.union(node - 1, node, parent, result)
        
        return result[0]

    def union(self, A, B, parent, result):
        a = self.find(A, parent)[0]
        b = self.find(B, parent)[0]
        if a < b:
            parent[b][0] = a
            parent[a][1] += parent[b][1]
            result[0] = max(result[0], parent[a][1])
        elif a > b:
            parent[a][0] = b
            parent[b][1] += parent[a][1]
            result[0] = max(result[0], parent[b][1])

    def find(self, node, parent):
        if node == parent[node][0]:
            return parent[node]
        parent[node] = self.find(parent[node][0], parent)
        return parent[node]