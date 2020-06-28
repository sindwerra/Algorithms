# coding=utf-8

'''
Given a sorted array of integers nums and integer values a, b and c. 
Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
'''

'''
稍有常识的人都知道... a大于零的函数有最小值，而a小于零有最大值，基于这一点就可以知道
a大于零是我们从两端开始判最大值放到结果数组最后，小于零则从两端判小值放到最开始
Beat 74.65%
公司：Google
'''

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        left, right = 0, n - 1
        f = lambda a, b, c, x : a * (x ** 2) + b * x + c

        if a == 0 and b >= 0:
            return [f(a, b, c, x) for x in nums]
        elif a == 0 and b < 0:
            return [f(a, b, c, nums[i]) for i in xrange(n - 1, -1, -1)]
        elif a < 0:
            while left <= right:
                x = f(a, b, c, nums[left])
                y = f(a, b, c, nums[right])
                if x < y:
                    res.append(x)
                    left += 1
                else:
                    res.append(y)
                    right -= 1
        else:
            while left <= right:
                x = f(a, b, c, nums[left])
                y = f(a, b, c, nums[right])
                if x > y:
                    res = [x] + res
                    left += 1
                else:
                    res = [y] + res
                    right -= 1
        
        return res