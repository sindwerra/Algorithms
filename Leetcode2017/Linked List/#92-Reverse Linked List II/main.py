# coding=utf-8

'''
Reverse a linked list from position m to n.
Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

'''
反转链表的实质是将pre点作为头并把链表扯为两段反转的
所以此处要把不反转的部分一头一尾保存起来，再把反转的一段和他们接上
Beat 48.90%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count, step = 1, n - m + 1
        cur = head
        pre, nxt = None, None
        while count < m:
            pre = cur
            cur = cur.next
            count += 1
        one, two = pre, cur
        pre, nxt = None, None
        while step:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            step -= 1
        if one:
            one.next = pre
        two.next = cur
        return head if one else pre
