# coding=utf-8

'''
There are N gas stations along a circular route, where
the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from station i to its next
station (i+1). You begin the journey with an empty tank
at one of the gas stations.

Return the starting gas station's index if you can travel
around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

'''
听九章讲座得到的答案，如果两个数组的差是小于零的那无路如何都不可能
有这样的位置，如果是大于等于零的则只需要遍历一遍找到从这个点开始
后面的点加起来的数都不小于零的位置就可以了
Beat 78.88%
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        tmp = [gas[i] - cost[i] for i in range(n)]
        if sum(tmp) < 0:
            return -1
        he, res = 0, 0
        st, ed = 0, n - 1
        while st <= ed:
            he += tmp[st]
            if he < 0:
                he, res = 0, st + 1
                if st > ed:
                    return -1
            st += 1
        return res
                
