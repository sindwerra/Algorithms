# coding=utf-8

# '''
# Sort a linked list in O(n log n) time using constant space complexity.
# '''

import operator

# Beat 95.89%

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        hst = {}
        kill = None

        # 解链

        while head != None:
            hst[head] = head.val
            kill = head
            head = head.next
            kill.next = None

        # 这里返回的是一个2元tuples的list，不能再dict化，那样相当于没做任何事

        sorted_x = sorted(hst.items(), key=operator.itemgetter(1))

        temp = None
        for s in sorted_x:
            if temp == None: temp = s[0]
            else:
                temp.next = s[0]
                temp = s[0]

        return sorted_x[0][0]
