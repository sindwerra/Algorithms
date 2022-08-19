# coding=utf-8

'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

'''
就是剑指offer那个很经典的题目，实际上就是把数字排序的比较标准由单纯的比大小变成了比较拼接之后比大小来
排序， Beat 60.19%
公司：Works Applications
'''

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        lst = sorted(nums, lambda x, y : cmp(str(x) + str(y), str(y) + str(x)))
        lst = [str(x) for x in lst]
        lst.reverse()
        result = int(''.join(lst))     # 为了防止有多个0或者头部有零的情况先用int parse一次再转回去
        return str(result)