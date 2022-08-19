# coding=utf-8

'''
中序遍历二叉树
'''

'''
正常的迭代中序遍历，一个stack和一个cur指针可以搞定，
时间复杂度O(n),空间复杂度O(h)
Beat 97.06%
公司：Microsoft
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

'''
Morris traversal,一种基于threaded tree的方法
时间复杂度O(n),空间复杂度O(1)
Beat 56.08%
'''

class Solution(object):
    def inorderTraversal(self, root):
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
            res.append(pre.val)
            pre = pre.right
