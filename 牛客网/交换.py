# coding=utf-8

# '''
# 请编写一个算法，不用任何额外变量交换两个整数的值。
# 给定一个数组num，其中包含两个值，请不用任何额外
# 变量交换这两个值，
# 并将交换后的数组返回。
# 测试样例：
# [1,2]
# 返回：[2,1]
# '''

# -*- coding:utf-8 -*-

class Swap:
    def getSwap(self, num):
        # write code here
        num[0] = num[0] ^ num[1]    # num[0]保存了两个数的信息
        num[1] ^= num[0]      # num[1]通过异或num[0]将本身的num[1]信息筛去变为num[0]
        num[0] ^= num[1]      # num[0]通过异或num[1]将num[0]信息筛去变为num[1]
       	return num
