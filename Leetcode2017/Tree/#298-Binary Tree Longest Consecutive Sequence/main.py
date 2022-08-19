# coding=utf-8

'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any
node in the tree along the parent-child connections. The longest consecutive
path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''

'''
O(n)时间复杂度就可以搞定
Beat 97.61%
公司：Google
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        pre = None
        self.helper(root, 0, pre, res)
        return res[0]

    def helper(self, root, count, pre, res):
        if not root:
            if count > res[0]:
                res.pop()
                res.append(count)
            return

        if pre == None:
            self.helper(root.left, count + 1, root, res)
            self.helper(root.right, count + 1, root, res)
        elif pre.val + 1 == root.val:
            self.helper(root.left, count + 1, root, res)
            self.helper(root.right, count + 1, root, res)
        else:
            if count > res[0]:
                res.pop()
                res.append(count)
            self.helper(root.left, 1, root, res)
            self.helper(root.right, 1, root, res)
