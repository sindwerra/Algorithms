# coding=utf-8

'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

'''
这题好像在牛客网上看过讲解，但不知道在哪里了
总结就是两个点不符合规律有两种情况（在中序遍历的情况下）
一种是整个树有两处不符合情况，第二种是只有一处不符合情况
第一种情况中，第一处不符合的点是较大的数，第二处是较小的数
第二种情况两个点互换就行
另外要求O(1) space, 所以用morris traversal, 且把收集点的步骤换成判断情况的代码
Beat 74.06%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        count= 0
        a, b, c = None, None, None
        pre, cur = root, None
        tmp = None
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

            if tmp and tmp.val > pre.val:
                if not count:
                    a, b = tmp, pre
                else:
                    c = pre
                count += 1

            tmp = pre
            pre = pre.right

        if count == 1:
            a.val, b.val = b.val, a.val
        else:
            a.val, c.val = c.val, a.val
