# coding=utf-8

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

'''
没有复杂算法， 快慢指针找到中点之后把后半部分反过来再归并就行了
Beat 87.76%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow = head
        
        if not head.next:
            return 
        
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left = head
        right = slow.next
        slow.next = None
        
        right = self.reverse(right)
        
        dummy = ListNode('dummy')
        cur = dummy
        count = 0
        
        while right:
            if count % 2 == 0:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
            count += 1
        
        if left:
            cur.next = left
            
    def reverse(self, root):
        pre, nxt = None, None
        while root:
            nxt = root.next
            root.next = pre
            pre = root
            root = nxt
        return pre    
        
        