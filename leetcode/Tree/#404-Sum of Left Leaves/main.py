# coding=utf-8

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree,
with values 9 and 15 respectively. Return 24.
'''

'''
删注释更健康，Beat 98.65%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        store = [root]
        if root == None: return 0
        res = 0
        while len(store) <> 0:
            tmp = store.pop()
            if tmp.right <> None: store.append(tmp.right)
            if tmp.left == None: continue
            if tmp.left.left == None and tmp.left.right == None:
                res += tmp.left.val
                continue
            if tmp.left <> None: store.append(tmp.left)

        return res
