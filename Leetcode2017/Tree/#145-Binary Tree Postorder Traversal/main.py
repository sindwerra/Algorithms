# coding=utf-8

'''
后序遍历的Morris版
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printEdge(self, root, lst):
        tail = self.reverseEdge(root)
        cur = tail
        while cur:
            lst.append(cur.val)
            cur = cur.right
        self.reverseEdge(tail)

    def reverseEdge(self, cur):
        pre, next = None, None
        while cur:
            next = cur.right
            cur.right = pre
            pre = cur
            cur = next
        return pre

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pre, cur = root, None
        res = []
        while pre:
            cur = pre.left
            if cur:
                while cur.right and cur.right != pre:
                    cur = cur.right
                if not cur.right:
                    cur.right = pre
                    pre = pre.left
                    continue
                else:
                    cur.right = None
                    self.printEdge(pre.left, res)
            pre = pre.right
        self.printEdge(root, res)
        return res
