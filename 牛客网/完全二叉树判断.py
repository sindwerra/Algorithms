# coding=utf-8

'''
有一棵二叉树,请设计一个算法判断它是否是完全二叉树。
给定二叉树的根结点root，请返回一个bool值代表它是否为完全二叉树。树的结点个数小于等于500。
'''

'''
flag用来判断是否到了临界节点（只有左子树或者第一个没有孩子的结点），层级遍历判断
'''

# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque as dq

class CheckCompletion:
    def chk(self, root):
        # write code here
        if not root: return True
        tmp = dq([root])
        flag = False
        while tmp:
            node = tmp.pop()
            if not flag:
                if not node.left and node.right:
                    return False
                if not node.right:
                    flag = True
            else:
                if node.left or node.right:
                    return False
            if node.left:
                tmp.appendleft(node.left)
            if node.right:
                tmp.appendleft(node.right)
        return True
