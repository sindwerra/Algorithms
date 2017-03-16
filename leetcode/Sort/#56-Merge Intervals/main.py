# coding=utf-8

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

'''
需要用到一个sorted函数依据关键字start来排序
没太多讲头，就是找区间合并就够了
Beat 79.73%
公司：LinkedIn, Google, Facebook, Twitter, Microsoft, Bloomberg, Yelp
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def returnStart(self, node):
        return node.start

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        lst = sorted(intervals, key = self.returnStart)
        res = []
        tmp = lst[0]
        for s in range(1, len(lst)):
            if tmp.end >= lst[s].start:
                if tmp.start <= lst[s].start and tmp.end >= lst[s].end:
                    continue
                elif tmp.start <= lst[s].start and tmp.end < lst[s].end:
                    tmp.end = lst[s].end
                elif tmp.start > lst[s].start and tmp.end >= lst[s].end:
                    tmp.start = lst[s].start
                elif tmp.start > lst[s].start and tmp.end < lst[s].end:
                    tmp.start = lst[s].start
                    tmp.end = lst[s].end
            else:
                ref = Interval(tmp.start, tmp.end)
                res.append(ref)
                tmp.start = lst[s].start
                tmp.end = lst[s].end
        res.append(tmp)
        return res
