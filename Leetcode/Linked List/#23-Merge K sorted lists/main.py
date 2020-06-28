# coding=utf-8

'''
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
'''

'''
这个题可以用最小堆做，也可以用分治法做，不过分治法肯定要快很多
这里用的是最小堆的做法
Beat 22.78%
公司：LinkedIn, Google, Uber, Airbnb, Facebook, Twitter, Amazon, Microsoft
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sf(self, lst, st, ed):
        while st <= ed:
            lf, rt = 2 * st + 1, 2 * st + 2
            mi = st
            if lf <= ed and lst[lf].val < lst[mi].val: mi = lf
            if rt <= ed and lst[rt].val < lst[mi].val: mi = rt
            if mi <> st:
                lst[st], lst[mi] = lst[mi], lst[st]
                st = mi
            else:
                break

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [x for x in lists if x]
        k = len(heap)
        for s in range(k / 2 - 1, -1, -1):
            self.sf(heap, s, k - 1)

        res = ListNode('dummy')
        cur = res

        while heap and heap[0].val != sys.maxint:
            cur.next = ListNode(heap[0].val)
            cur = cur.next
            if heap[0].next:
                heap[0] = heap[0].next
            else:
                heap[0] = ListNode(sys.maxint)
            self.sf(heap, 0, k - 1)
        return res.next


'''
下面是分治的做法，结果比最小堆还慢啊...
Beat 13.06%
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode('dummy')
        cur = res
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = ListNode(l2.val)
            l2 = l2.next
            cur = cur.next
        return res.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if not n:
            return None
        if n == 1 and lists[0]:
            return lists[0]
        if n == 1 and not lists[0]:
            return None
        a = self.mergeKLists(lists[:n / 2])
        b = self.mergeKLists(lists[n / 2:])
        return self.mergeTwoLists(a, b)


'''
下面是一些用了现成库的方法
'''

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

'''
用了heapq的方法
'''

def mergeKLists(self, lists):
    from heapq import heappush, heappop, heapreplace, heapify
    dummy = node = ListNode(0)
    h = [(n.val, n) for n in lists if n]
    heapify(h)
    while h:
        v, n = h[0]
        if n.next is None:
            heappop(h) #only change heap size when necessary
        else:
            heapreplace(h, (n.next.val, n.next))
        node.next = n
        node = node.next

    return dummy.next
