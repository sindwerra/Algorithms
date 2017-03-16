# coding=utf-8

'''
Given an array of integers, every element appears three times
except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

'''

'''
此种方法极易理解，而且有很强的普适性，只要题干要求是一个数组所有数
都出现K次除了一个数只出现一次，都可以用这个方法，只要把mod的数改成
K就行了，不过此方法在找负数时会返回负数的反码，一旦元素的值超过某个范围
此方法就不能用了
Beat 21.12%
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            base = 1 << i
            sum = 0
            for j in range(len(nums)):
                if nums[j] & base:
                    sum += 1
            if sum % 3:
                res |= base
        return res if abs(res) < abs(res - 2 ** 32) else res - 2 ** 32

'''
一个更快而且更坚固的方法，但是没有什么道理可讲，纯粹是凑出来的
Beat 88.41%
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0
