# coding=utf-8

'''
Given a binary search tree (BST) with duplicates,
find all the mode(s) (the most frequently occurred element)
in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less
than or equal to the node's key.
The right subtree of a node contains only nodes with keys
greater than or equal to the node's key.
Both the left and right subtrees must also be binary search
trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them
in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
'''

'''
这要求的follow up感觉没法做到啊，只要存在多个mode就不可能不用extra space的
Beat 80.50%
公司：Google
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, store = [], {}
        count = -sys.maxint
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if store.has_key(root.val):
                    store[root.val] += 1
                else:
                    store[root.val] = 1
                if store[root.val] > count:
                    count = store[root.val]
                root = root.right

        res = []

        for s in store:
            if store[s] == count:
                res.append(s)
        return res
