# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Palindrome:
    def isPalindrome(self, pHead):
        # write code here
        lst = []
        # head = pHead
        while pHead != None:
            lst.append(pHead.val)   # 必须放第一行
            pHead = pHead.next

        for s in range(len(lst) / 2):
            if lst[s] != lst[- s - 1]: return False

        return True
