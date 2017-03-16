# coding=utf-8

'''
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of
the linked list. If the number of nodes is not a multiple of k then
left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

'''
此题需要四个指针,tmp作为每一轮的头指针,cur作为活动指针，root作为反过来后的头指针
tail作为反过来之前的头指针，res就是最后个结果头指针
Beat 74.61%
公司：Microsoft, Facebook
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head, count):
        pre, nxt = None, None
        while count:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
            count -= 1
        return pre

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        cur = head
        tmp = head
        root, tail = None, head
        res = head
        while cur:
            count += 1
            if count == k:
                cur = cur.next
                if not root:
                    res = self.reverse(tmp, k)
                    root = res
                else:
                    root = self.reverse(tmp, k)
                    tail.next = root
                    tail = tmp

                tmp.next = cur
                tmp = tmp.next
                count = 0
                continue
            else:
                cur = cur.next
        return res
