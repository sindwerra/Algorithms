# coding=utf-8

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common
ancestor is defined between two nodes v and w as the lowest node in
T that has both v and w as descendants (where we allow a node to be
a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5, since a node can be a
descendant of itself according to the LCA definition.
'''

'''
暂时就只想出来这种方法，因为这不是完全二叉树，所以层级遍历的方法不能用
只能用递归两边分别收集这两个点所在的路径最后进行比较
Beat 35.19%
公司：Amazon, LinkedIn, Apple, Facebook, Microsoft
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, target, lst):
        if not root:
            return False
        if root == target:
            lst.append(root)
            return True
        lst.append(root)
        a, b = self.helper(root.left, target, lst), self.helper(root.right, target, lst)
        if not a and not b:
            lst.pop()
            return False
        return True

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        one, two = [], []
        self.helper(root, p, one)
        self.helper(root, q, two)
        n, m = len(one), len(two)
        if n <= m:
            st = 0
            while st <= n - 1:
                if one[st] != two[st]:
                    return one[st - 1]
                st += 1
            return one[st - 1]
        else:
            st = 0
            while st <= m - 1:
                if two[st] != one[st]:
                    return two[st - 1]
                st += 1
            return two[st - 1]
