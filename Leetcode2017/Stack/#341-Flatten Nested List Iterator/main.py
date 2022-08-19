# coding=utf-8

'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: 
[1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should 
be: [1,4,6].
'''

'''
用的就是跟Nested List Weight Sum一样的思路，其实和排列组合的题差不多，不过有没有真正的类似Python里面generator一样的算法呢
Beat 82.98%
公司：Google, Facebook, Twitter
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.store = []
        
        for nestedNum in nestedList:
            self.store.extend(self.helper(nestedNum))
        
        self.cursor = -1
        self.limit = len(self.store)
    
    def helper(self, nestedNum):
        if nestedNum.isInteger():
            return [nestedNum.getInteger()]
            
        result = []
        
        for num in nestedNum.getList():
            result.extend(self.helper(num))
            
        return result
            
    def next(self):
        """
        :rtype: int
        """
        self.cursor += 1
        return self.store[self.cursor]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor + 1 < self.limit

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())