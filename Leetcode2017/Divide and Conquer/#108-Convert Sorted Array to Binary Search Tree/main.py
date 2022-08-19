# coding=utf-8

'''
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
'''

'''
还是分治思路，每次找数组的中间点，然后左右两部分分开递归向下
Beat 87.13%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        st, ed = 0 , len(nums) - 1
        mid = (st + ed) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
