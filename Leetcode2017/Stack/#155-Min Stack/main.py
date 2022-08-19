# coding=utf-8

'''
# // Design a stack that supports push, pop, top, and retrieving the minimum
# // element in constant time.
# //
# // push(x) -- Push element x onto stack.
# // pop() -- Removes the element on top of the stack.
# // top() -- Get the top element.
# // getMin() -- Retrieve the minimum element in the stack.
# // Example:
# // MinStack minStack = new MinStack();
# // minStack.push(-2);
# // minStack.push(0);
# // minStack.push(-3);
# // minStack.getMin();   --> Returns -3.
# // minStack.pop();
# // minStack.top();      --> Returns 0.
# // minStack.getMin();   --> Returns -2.
'''

'''
公司：Google, Uber, Zenefits, Amazon, Snapchat, Bloomberg
'''

# 用list就行了

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallest = float('inf')
        self.store = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.smallest: self.smallest = x
        self.store.append(x)


    def pop(self):
        """
        :rtype: void
        """
        trash = self.store.pop()
        if trash == self.smallest: self.smallest = self.__findSmallest__(self.store)


    def top(self):
        """
        :rtype: int
        """
        return self.store[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.smallest

    def __findSmallest__(self, lst):
        result = float('inf')
        for s in lst:
            if s < result: result = s
        return result

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
另一种利用双栈来实现min stack的方法，Beat 91.65%
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a, self.b = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.a.append(x)
        if not self.b:
            self.b.append(x)
        else:
            if x < self.b[-1]:
                self.b.append(x)
            else:
                node = self.b[-1]
                self.b.append(node)

    def pop(self):
        """
        :rtype: void
        """
        self.a.pop()
        self.b.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.b[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
