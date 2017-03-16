'''
题目描述
编写代码，以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前
给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。
注意：分割以后保持原来的数据顺序不变。
'''

'''
拆开再合并
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Partition:
    def partition(self, pHead, x):
        # write code here
        left, right = [], []
        while pHead:
            cur = pHead
            if pHead.val < x:
                left.append(cur)
            else:
                right.append(cur)
            pHead = pHead.next
        left += right
        for s in range(len(left) - 1):
            left[s].next = left[s + 1]
        left[-1].next = None
        return left[0]
