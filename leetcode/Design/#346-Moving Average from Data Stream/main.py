# coding=utf-8

'''
Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

'''
用队列就行，Beat 60.10%
'''

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.store = collections.deque([])
        self.n, self.size = 0, size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.n += 1
        self.store.appendleft(val)
        if self.n > self.size:
            self.n = self.size
            self.store.pop()
        return sum(self.store) / float(self.n)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
