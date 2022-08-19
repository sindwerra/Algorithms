# coding=utf-8

'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
'''

'''
既然不是array，变成array再做就行了哈哈哈
Beat 70.16%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return self.sortedArrayToBST(lst)
