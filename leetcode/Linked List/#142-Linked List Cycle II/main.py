# coding=utf-8

'''
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

'''
Runner Technique的经典应用，一快一慢的指针若有循环必然相遇，且相遇点
与循环开始结点的距离必然等于头结点到循环开始点的距离，Beat 76.43%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        rabbit, turtle = head, head
        count = 0
        while count <= 1:       # 一开始是相遇的，必须判断第二次相遇
            if turtle == rabbit:
                count += 1
            if not rabbit:      # rabbit已经为空了，无循环
                return None
            if not rabbit.next: # rabbit下一个为空，也是无循环
                return None
            if count > 1:
                break
            rabbit = rabbit.next.next
            turtle = turtle.next

        cur = head              # 一个新指针从头推，相遇点即为结点
        while cur != rabbit:
            cur = cur.next
            rabbit = rabbit.next
        return cur

'''
不太容易理解的一种版本，Beat 87.29%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rabbit, turtle = head, head
        count = 0
        while turtle:
            if turtle == rabbit:
                count += 1
            if not turtle.next:
                return None
            if count > 1:
                break
            turtle = turtle.next.next
            rabbit = rabbit.next
            if not turtle:
                return None

        cur = head
        while cur != turtle:
            cur = cur.next
            turtle = turtle.next
        return cur
