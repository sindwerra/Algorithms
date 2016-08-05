# coding=utf-8

# '''
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
# '''

# 利用修改node的值来判断是否链表有循环结构，Beat 16.89%

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        itr = head
        while itr != None:
            if itr.val == 'X': return True
            else:
                itr.val = 'X'
                itr = itr.next

        return False
