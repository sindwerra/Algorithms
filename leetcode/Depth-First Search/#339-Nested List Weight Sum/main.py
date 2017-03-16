# coding=utf-8

'''
Given a nested list of integers, return
the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10.
(four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27.
(one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3;
1 + 4*2 + 6*3 = 27)
'''

'''
利用内存做一个大栈来求就行，Beat 41.07%，可能用迭代会快很多

公司：LinkedIn
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def DS(self, target, lst, count):
        if not target:
            return
        if not target[-1].isInteger():
            self.DS(target[-1].getList(), lst, count + 1)
        else:
            lst[0] += target[-1].getInteger() * count
        target.pop()
        self.DS(target, lst, count)

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = [0]
        self.DS(nestedList, res, 1)
        return res[0]
