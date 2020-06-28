# coding=utf-8

'''
Given a binary tree where all the right nodes are either leaf nodes with a sibling 
(a left node that shares the same parent node) or empty, flip it upside down and turn it into 
a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
'''

'''
这里说的树是一种很特殊的树，它的所有右孩子要不是有左兄弟的叶子节点，要不就是空的，也就意味着正常遍历在到达最左结点
时所有的树上的结点都已经被压入stack中了，导致可以一次完成所有的翻转而不会出现因为结构破坏而找不到其他结点的情况
基本的思路就是Divide and Conquer了
Beat 67.36%
公司：LinkedIn
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        head = root
        while head.left != None:
            head = head.left
        self.helper(root)
        return head
    
    def helper(self, root):    
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        a = root
        b = self.helper(root.left)
        c = self.helper(root.right)
        a.left = None
        a.right = None
    
        b.left = c
        b.right = a
    
        return a