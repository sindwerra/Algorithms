# coding=utf-8

'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

# 情况很多

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # 其实是用来找结点的后继点

    def inOrder(self, Node):
        if Node.left == None: return Node
        return self.inOrder(Node.left)

    def GetNext(self, pNode):
        # write code here
        if pNode == None: return None     # 树不存在
        if pNode.right <> None: return self.inOrder(pNode.right)  # 结点有右孩子
        if pNode.next == None: return None   # 结点为根节点且无右孩子
        elif pNode.next.left == pNode: return pNode.next  # 结点本身是一个左孩子
        else:
            if pNode.next.next <> None:                   # 结点的父节点是一个左孩子
                if pNode.next == pNode.next.next.left:
                    return pNode.next.next
                else:
                    return None
            else: return None
