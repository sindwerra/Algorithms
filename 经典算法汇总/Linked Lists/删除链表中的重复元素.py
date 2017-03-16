# coding=utf-8

'''
经典算法，删除链表中的重复元素，有重复出现的可能
删除链表中等于给定值val的所有节点。
给出链表 1->2->3->3->4->5->3, 和 val = 3,
你需要返回删除3之后的链表：1->2->4->5。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if not head:
            return head
        dummy = ListNode('a')
        dummy.next = head
        cur = dummy
        while cur:
            if cur.next and cur.next.val == val:
                tmp = cur.next
                while tmp and tmp.val == val:
                    tmp = tmp.next
                cur.next = tmp
            cur = cur.next
        return dummy.next
