# coding=utf-8

'''
Given an array of numbers nums, in which exactly
two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important.
So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
'''

# 用的牛客网上面讲的思路，头一遍异或找出两个值合并的信息，再从此值里找二进制中出现的第一个1
# 这里注意从低位往高位找才行，然后拿找到的index再去遍历list将所有此位带1的数全部异或一遍
# 就找到其中一个数了
# Beat 53.44%

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        combine = 0
        for a in nums:
            combine ^= a

        string = bin(combine)[2:].zfill(32)

        index = 0
        for s in xrange(31, -1, -1):
            if string[s] == '1':
                index = s

        tmp = 0
        for b in nums:
            string = bin(b)[2:].zfill(32)
            if string[index] == '1':
                tmp ^= b

        return [tmp, combine^tmp]
