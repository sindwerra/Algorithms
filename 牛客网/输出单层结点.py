# coding=utf-8

'''
对于一棵二叉树，请设计一个算法，创建含有某一深度上所有结点的链表。
给定二叉树的根结点指针TreeNode* root，以及链表上结点的深度，请返回一个链表ListNode，
代表该深度上所有结点的值，请按树上从左往右的顺序链接，保证深度不超过树的高度，
树上结点的值为非负整数且不超过100000。
'''

'''
层级遍历的变形题而已
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class TreeLevel:
    def getTreeLevel(self, root, dep):
        # write code here
        if root == None: return None
        cur, nxt = collections.deque([root]), collections.deque([])
        tmp = []
        count = 1
        while len(cur):
            node = cur.pop()
            if node:
                a = ListNode(node.val)
                tmp.append(a)
                if node.left:
                    nxt.appendleft(node.left)
                if node.right:
                    nxt.appendleft(node.right)
            if len(cur) == 0:
                if count == dep:
                    break
                tmp = []
                cur, nxt = nxt, cur
                count += 1

        for index in xrange(len(tmp) - 1):
            tmp[index].next = tmp[index + 1]
        return tmp[0]
