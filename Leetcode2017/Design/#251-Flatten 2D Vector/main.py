# coding=utf-8

'''
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:
How many variables do you need to keep track?
Two variables is all you need. Try with x and y.
Beware of empty rows. It could be the first few rows.
To write correct code, think about the invariant to maintain. What is it?
The invariant is x and y must always point to a valid point in the 2d vector.
Should you maintain your invariant ahead of time or right when you need it?
Not sure? Think about how you would implement hasNext(). Which is more complex?
Common logic in two different places should be refactored into a common method.
Follow up:
As an added challenge, try to code it using only iterators
in C++ or iterators in Java.
'''

'''
注意最后一个值时的情况就好，Beat 87.50%
公司：Google, Airbnb, Twitter, Zenefits
'''

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.store = []
        for s in vec2d:
            self.store += s
        self.n = len(self.store)
        self.count = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            res = self.store[self.count]
            self.count += 1
            return res
        else:
            return


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count <= self.n - 1

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
