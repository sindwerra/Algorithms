# coding=utf-8

'''
Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

# 就是单独写个函数用字符串记录结果最后相加就行了啊
# Beat 99.25%，为什么这么快呢，我自己也想不通啊...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def REC(self, root, base, lst):
        if root == None: return
        base += str(root.val)
        if root.left == None and root.right == None:
            lst.append(int(base))
        self.REC(root.left, base, lst)
        self.REC(root.right, base, lst)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        base, lst = '', []
        self.REC(root, base, lst)
        return sum(lst)
