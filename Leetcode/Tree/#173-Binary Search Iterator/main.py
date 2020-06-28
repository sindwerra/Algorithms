# coding=utf-8

'''
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1)
time and uses O(h) memory, where h is the height of the tree.
'''

'''
BST的中序序列化然后用count=list长度来判断是否能next就行，Beat 64.51%
'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = []
        self.in_ord(root, self.lst)
        self.count = len(self.lst)
        self.n = self.count

    def in_ord(self, root, lst):
        if root == None: return lst
        self.in_ord(root.left, lst)
        lst.append(root.val)
        self.in_ord(root.right, lst)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count != 0

    def next(self):
        """
        :rtype: int
        """
        res = self.lst[self.n - self.count]
        self.count -= 1
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
