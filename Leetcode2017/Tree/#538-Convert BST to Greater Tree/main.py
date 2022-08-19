# coding=utf-8

'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the 
original BST is changed to the original key plus sum of all keys greater than the original 
key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

'''
反向的中序遍历可以解决
公司：Amazon
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        count = None
        stack = []
        head = root
        
        while head or stack:
            if head:
                stack.append(head)
                head = head.right
            else:
                head = stack.pop()
                if count == None:
                    count = head.val
                else:
                    count += head.val
                    head.val = count
                head = head.left
        
        return root
                