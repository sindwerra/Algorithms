# coding=utf-8

'''
A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

'''
牛客网介绍的O(1)空间复杂度算法，头一遍遍历把每一个结点拷贝一个新节点到这个结点后面
第二遍遍历利用两个结点相邻的关系拷贝原结点的随机结点
第三遍遍历将拷贝的结点全部拿下来返回
这应该是最优解了
Beat 95.24%
公司：Amazon, Microsoft, Bloomberg, Uber (亚马逊OA九题之一)
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            node = RandomListNode(cur.label)
            tmp = cur.next
            cur.next = node
            node.next = tmp
            cur = cur.next.next

        count, pre, cur = 0, None, head
        while cur:
            if count:
                cur.random = pre.random.next if pre.random else None
                count = -1
            count += 1
            pre = cur
            cur = cur.next

        count, pre, cur = 0, None, head
        res = RandomListNode(5)
        tmp = res
        while cur:
            if count:
                pre.next = cur.next
                tmp.next = cur
                tmp = tmp.next
                count = -1
            count += 1
            pre = cur
            cur = cur.next
        return res.next
