# coding=utf-8

'''
You are given two linked lists representing two non-negative numbers.
The most significant digit comes first and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words,
reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

'''
好鸡巴恶心啊... Beat 40.96%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b = l1, l2
        lf, rt = [], []
        while a or b:
            if a:
                lf.append(a.val)
                a = a.next
            if b:
                rt.append(b.val)
                b = b.next

        col = 1
        one = 0
        for s in xrange(len(lf) - 1, -1, -1):
            one += (col * lf[s])
            col *= 10

        col = 1
        for s in xrange(len(rt) - 1, -1, -1):
            one += (col * rt[s])
            col *= 10

        if one == 0: return ListNode(0)
        end = None
        while one > 0:
            rem = one % 10
            one = (one - rem) / 10
            cur = ListNode(rem)
            cur.next = end
            end = cur
        return end
        
