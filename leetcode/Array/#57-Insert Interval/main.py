# coding=utf-8

'''
Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to
their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in
as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

'''
这题也没什么特别难得地方，把六种情况仔细分开就好
Beat 48.62%
公司：LinkedIn, Google, Facebook
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        step = 0
        base = newInterval
        flag = True

        while step <= n - 1:
            if base.end < intervals[step].start:
                break
            elif base.start <= intervals[step].start and base.end >= intervals[step].start and base.end <= intervals[step].end:
                base.end = intervals[step].end
                del intervals[step]
                break
            elif base.start < intervals[step].start and base.end > intervals[step].end:
                del intervals[step]
                step -= 1
                n -= 1
            elif base.start >= intervals[step].start and base.end <= intervals[step].end:
                flag = False
                break
            elif base.start >= intervals[step].start and base.start <= intervals[step].end and base.end >= intervals[step].end:
                base.start = intervals[step].start
                del intervals[step]
                step -= 1
                n -= 1

            step += 1


        if flag:
            intervals.insert(step, base)
        return intervals
