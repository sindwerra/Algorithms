# coding=utf-8

'''
给出飞机的起飞和降落时间的列表，用 interval 序列表示. 请计算出天上同时最多有多少架飞机？

 注意事项

如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

您在真实的面试中是否遇到过这个题？ Yes
样例
对于每架飞机的起降时间列表：[[1,10],[2,3],[5,8],[4,7]], 返回3。
'''

'''
区间扫描线问题，将所有时间戳全部拆开排序即可
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def comparator(self, A, B):
        if A[0] > B[0]:
            return 1
        elif A[0] < B[0]:
            return -1
        elif A[1] == True and B[1] == False:
            return 1
        elif A[1] == False and B[1] == True:
            return -1
        else:
            return 0

    def countOfAirplanes(self, airplanes):
        # write your code here
        tmp = []
        
        for airplane in airplanes:
            tmp.append([airplane.start, True])
            tmp.append([airplane.end, False])
        
        tmp.sort(self.comparator)

        result = 0
        cur_count = 0
        for tag in tmp:
            if tag[1]:
                cur_count += 1
            else:
                cur_count -= 1
            result = max(result, cur_count)
        
        return result