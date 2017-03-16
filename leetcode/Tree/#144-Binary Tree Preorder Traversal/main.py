# coding=utf-8

'''
非递归二叉树前序遍历
'''

'''
传统迭代前序遍历
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

'''
Morris Traversal 版，不过此版会有破坏树结构
'''

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pre, cur = root, None
        res = []
        while pre:
            cur = pre.left
            res.append(pre.val)
            if cur:
                while cur.right and cur.right != pre.right:
                    cur = cur.right
                if not cur.right:
                    cur.right = pre.right
                    pre = pre.left
                    continue
                # else:                 # 这行可以去掉，因为是破坏性算法，不会有这种情况
                #     cur.right = None
            pre = pre.right
        return res

'''
不破坏结构的Morris Traversal
'''

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur1, cur2 = root, None
        res = []
        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right != cur1:
                    cur2 = cur2.right
                if not cur2.right:
                    cur2.right = cur1
                    res.append(cur1.val)
                    cur1 = cur1.left
                    continue
                else:
                    cur2.right = None
            else:
                res.append(cur1.val)
            cur1 = cur1.right
        return res
