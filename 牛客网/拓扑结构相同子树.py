# coding=utf-8

'''
对于两棵彼此独立的二叉树A和B，请编写一个高效算法，
检查A中是否存在一棵子树与B树的拓扑结构完全相同。
给定两棵二叉树的头结点A和B，请返回一个bool值，代表A中是否存在一棵同构于B的子树。
'''

'''
将两颗二叉树序列化后转换为string模式查找问题，序列化必须用前序遍历
并且对空节点也要做加值处理不能直接返回,用string变量序列化再用KMP算法是最快方式
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class IdenticalTree:
    def in_order(self, root, lst):
        if root == None:
            lst.append('N')
            return
        lst.append(root.val)
        self.in_order(root.left, lst)
        self.in_order(root.right, lst)

    def chkIdentical(self, A, B):
        # write code here
        lst_A, lst_B = [], []
        self.in_order(A, lst_A)
        self.in_order(B, lst_B)
        n, m = len(lst_A), len(lst_B)

        # 这里只用了朴素字串查找方法

        for s in xrange(n - m + 1):
            if lst_A[s:s + m] == lst_B:
                return True
        return False

# 一种更快的参考方案

class IdenticalTree:
    def chkIdentical(self, A, B):
        listA=self.listTree(A)
        listB=self.listTree(B)
        if listB in listA:
            return True
        else:
            return False

    def listTree(self,A):
        if A==None:
            return "#!"
        string=str(A.val)+"!"
        string+=self.listTree(A.left)
        string+=self.listTree(A.right)
        return string
