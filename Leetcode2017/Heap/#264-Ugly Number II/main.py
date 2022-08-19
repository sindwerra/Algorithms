# coding=utf-8

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

'''
看九章做的，这题最显然的做法就是heap了，但是速度肯定也最慢，反正把每个弹出的数分别乘2，3，5丢进堆里就好
另外checker查重，Beat 8.55%
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        heap = [1]
        lst = [2, 3, 5]
        checker = {}
        
        for i in xrange(n):
            base = heapq.heappop(heap)
            for mul in lst:
                self.checkAndInsert(checker, base, heap, mul)
        
        return base
        
    def checkAndInsert(self, checker, base, heap, mul):
        a = base * mul
        if checker.has_key(a):
            return 
        checker[a] = 1
        heapq.heappush(heap, a)
        
        
            
        
        
        
        