'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        # python用的是额外的list数据结构储存tree node的值然后再与排序后的list对比
        # 一样的话即为BST

class Solution(object):
    def IVB(self, root, lst):
        if root == None: return
        self.IVB(root.left, lst)
        lst.append(root.val)
        self.IVB(root.right, lst)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lst = []
        self.IVB(root, lst)
        temp = sorted(lst)
        for s in range(len(lst) - 1):
            if lst[s] == lst[s + 1]: return False  # 考虑相邻两数相等的情况
            if lst[s] != temp[s]: return False

        if len(lst) == 0: return True     # 考虑树为空的情况

        return True and (lst[-1] == temp[-1])
