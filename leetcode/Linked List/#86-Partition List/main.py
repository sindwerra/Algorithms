# coding=utf-8

'''
Given a linked list and a value x, partition it such that
all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in
each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

'''
貌似用的是原始快排的思维？基本就是一遍遍历，两个list，小的放左，大的放右
然后将两个list合并成一个重构一个新的linked list即可
Beat 75.23%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        llst, rlst = [], []
        cur = head
        if head == None: return None
        count = 0
        while cur != None:
            count += 1
            tmp = ListNode(cur.val)
            if tmp.val < x:
                llst.append(tmp)
            else:
                rlst.append(tmp)
            cur = cur.next
        llst += rlst
        for s in xrange(count - 1):
            llst[s].next = llst[s + 1]
        return llst[0]

class Solution(object):
    def partition(self, Head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not Head: return []
        left, right = [], []
        count = 0
        while Head:
            cur = Head
            if Head.val < x:
                left.append(cur)
            else:
                right.append(cur)
            Head = Head.next
            count += 1
        left += right
        for s in range(count - 1):
            left[s].next = left[s + 1]
        left[-1].next = None
        return left[0]
