'''
实现一个函数，检查二叉树是否平衡，平衡的定义如下，对于树中的任意一个结点，
其两颗子树的高度差不超过1。
给定指向树根结点的指针TreeNode* root，请返回一个bool，代表这棵树是否平衡。
'''

'''
左子树高度，右子树高度，总高度三个参数判断平衡性
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Balance:
    def height(self, root):
        if root == None: return (0, True)
        lh = self.height(root.left)
        rh = self.height(root.right)
        return (max(lh[0], rh[0]) + 1, abs(lh[0] - rh[0]) <= 1 and lh[1] and rh[1])

    def isBalance(self, root):
        # write code here
        if root == None: return True
        lf = self.height(root.left)
        rt = self.height(root.right)
        return (abs(lf[0] - rt[0]) <= 1) and lf[1] and rt[1]
