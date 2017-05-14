# coding=utf-8

'''
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''

'''
跟数飞机问题一模一样，换了个描述而已，标准扫描线问题，比较器很影响速度
Beat 8.27%
公司：Google, Snapchat, Facebook
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def comparator(self, A, B):
        if A[0] < B[0]:
            return -1
        elif A[0] > B[0]:
            return 1
        elif A[1] == True and B[1] == False:
            return 1
        elif A[1] == False and B[1] == True:
            return -1
        else:
            return 0

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        tmp = []
        for interval in intervals:
            tmp.append([interval.start, True])
            tmp.append([interval.end, False])
        
        tmp.sort(self.comparator)

        result = -sys.maxint
        cur_count = 0
        for tag in tmp:
            if tag[1]:
                cur_count += 1
            else:
                cur_count -= 1
            result = max(result, cur_count)
        
        return result if result != -sys.maxint else 0