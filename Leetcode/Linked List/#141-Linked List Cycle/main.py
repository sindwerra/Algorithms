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

'''
不需要修改值也不需要额外空间就能判断的另外一种方法，双指针一快一慢
Beat 29.64%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rabbit, turtle = head, head
        count = 0
        while turtle:
            if turtle == rabbit:
                count += 1
            if count > 1:
                return True
            if not turtle.next:
                return False
            turtle = turtle.next.next
            rabbit = rabbit.next
        return False
