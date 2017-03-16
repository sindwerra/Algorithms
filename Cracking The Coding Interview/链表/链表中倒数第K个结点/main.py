# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None: return None
        lst = []
        while head != None:
            lst.append(head)
            head = head.next

        if k > len(lst) or k <= 0: return None

        return lst[- k]
