# coding=utf-8

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
 digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

'''
一位位进就可以，最后有个进位需要再检查一遍，Beat 61.81%
公司：Amazon, Microsoft, Bloomberg, Airbnb, Adobe
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, a, b):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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
