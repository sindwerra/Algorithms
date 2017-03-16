'''
题目描述
有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，
也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。
给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。
测试样例：
{1,2,3},{3,2,1}
返回：{4,4,4}
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Plus:
    def plusAB(self, a, b):
        # write code here
        step = 0
        dummy = ListNode(0)
        cur = dummy
        while a or b:
            if not a:
                node = ListNode((b.val + step) % 10)
                step = (b.val + step) / 10
                b = b.next
            elif not b:
                node = ListNode((a.val + step) % 10)
                step = (a.val + step) / 10
                a = a.next
            else:
                node = ListNode((a.val + b.val + step) % 10)
                step = (a.val + b.val + step) / 10
                a, b = a.next, b.next
            cur.next = node
            cur = cur.next
        if step:
            cur.next = ListNode(step)
        return dummy.next
