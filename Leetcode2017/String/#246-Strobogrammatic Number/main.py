# coding=utf-8

'''
A strobogrammatic number is a number that looks the same when
rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''

'''
反过来之后从后到前比较就行，180不用care，69位置要互换，其他数字不能出现
Beat 22.90%
改进版用dict存储01689再来查询快很多，Beat 92.29%
公司：Google
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        cp = ''
        for index in range(len(num) - 1, -1, -1):
            if num[index] not in '01689':
                return False
            if num[index] == '6':
                cp += '9'
            elif num[index] == '9':
                cp += '6'
            else:
                cp += num[index]
        return cp == num

'''
改进版用dict存
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        cp = ''
        store = {'0':1,'1':1,'6':1,'8':1,'9':1}
        for index in range(len(num) - 1, -1, -1):
            if not store.has_key(num[index]):
                return False
            if num[index] == '6':
                cp += '9'
            elif num[index] == '9':
                cp += '6'
            else:
                cp += num[index]
        return cp == num
