# coding=utf-8

'''
Given an array of meeting time intervals consisting of start and
end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person
could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''

'''
先按照起始时间排个序，Beat 0.79%，这也太慢了吧...
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def qs(self, lst):
        if len(lst) <= 1: return lst
        else:
            pivot = lst[0].start
            return self.qs([x for x in lst[1:] if x.start < pivot]) + [lst[0]] + self.qs([x for x in lst[1:] if x.start >= pivot])

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        lst = self.qs(intervals)
        for s in range(0, len(lst) - 1):
            if lst[s].end > lst[s + 1].start:
                return False
        return True
