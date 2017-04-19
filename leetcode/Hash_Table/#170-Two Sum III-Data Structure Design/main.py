# coding=utf-8

'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
'''

'''
这题主要要明确add函数耗费不能大，另外哈希表必须要用到
Beat 28.91%
公司：LinkedIn
'''


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        self.nums = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums.append(number)
        if not self.store.has_key(number):
            self.store[number] = 1
        else:
            self.store[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            if value - num == num:
                if self.store[num] > 1:
                    return True
                continue
            elif self.store.has_key(value - num):
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)