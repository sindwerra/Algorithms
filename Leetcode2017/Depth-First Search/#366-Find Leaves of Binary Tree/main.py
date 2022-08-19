# coding=utf-8

'''
Given a binary tree, collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
          1
         / \
        2   3
       / \
      4   5
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2
2. Now removing the leaf [2] would result in this tree:

          1
3. Now removing the leaf [1] would result in the empty tree:

          []
Returns [4, 5, 3], [2], [1].
'''

'''
这道题不考察顺序，可以通过反复前序遍历并加上一个附加条件来收集node
不过这种做法对树是有破坏性的，且不是按照从左到右的顺序收集node
Beat 82.27%
公司：Linkedin
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        a = []
        res, tmp = [], []
        while root.left or root.right:
            a = [root]
            while a:
                node = a.pop()
                if node.left:
                    if not node.left.left and not node.left.right:
                        tmp.append(node.left.val)
                        node.left = None
                    else:
                        a.append(node.left)
                if node.right:
                    if not node.right.left and not node.right.right:
                        tmp.append(node.right.val)
                        node.right = None
                    else:
                        a.append(node.right)
            res.append(tmp)
            tmp = []
        tmp = [root.val]
        res.append(tmp)
        return res
