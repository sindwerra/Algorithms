# coding=utf-8

'''
Given a non-negative number represented as a singly linked list of digits,
plus one to the number.

The digits are stored such that the most significant digit is
 at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
'''

'''
用栈往回倒就行，应该有其他方法可以做，Beat 29.66%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        stack, cur = [], head
        while cur:
            stack.append(cur)
            cur = cur.next

        step = True
        while step and len(stack):
            node = stack.pop()
            if node.val < 9:
                node.val += 1
                step = False
            else:
                node.val = 0

        if step:
            new_head = ListNode(1)
            new_head.next = head
            return new_head
        return head
