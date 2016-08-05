# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA, countB = 0, 0
        temp1, temp2 = headA, headB

        if temp1 == None or temp2 == None: return None
        while temp1 != None or temp2 != None:
            if temp1 != None:
                temp1 = temp1.next
                countA += 1
            if temp2 != None:
                temp2 = temp2.next
                countB += 1

        temp1, temp2 = headA, headB

        if countA > countB:
            for s in range(countA - countB): temp1 = temp1.next
            for a in range(countB):
                if temp1 == temp2: return temp1
                temp1, temp2 = temp1.next, temp2.next
        else:
            for s in range(countB - countA): temp2 = temp2.next
            for a in range(countA):
                if temp1 == temp2: return temp2
                temp1, temp2 = temp1.next, temp2.next

        return None
