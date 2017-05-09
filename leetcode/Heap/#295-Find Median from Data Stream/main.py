# coding=utf-8

'''
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''

'''
简单讲就是一个最大堆和一个最小堆维护，不过最大堆必须要用取反来维护
Beat 91.56%
公司：Google
'''

class MedianFinder(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif not self.min_heap:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif self.count % 2 == 0:
            if num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
                tmp = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -tmp)

        self.count += 1
        
    def findMedian(self):
        """
        :rtype: float
        """
        if not self.min_heap or self.count % 2:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()