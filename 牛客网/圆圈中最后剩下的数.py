# coding=utf-8

'''
题目描述

每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:
首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,
可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,
哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''

'''
还没想到数学方法解决这道题，现有的是通过list来判断的，速度太慢了
'''

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0: return -1
        ref = n * (n - 1) / 2
        count = 0
        index = 0
        while n > 1:
            if count == m - 1:
                del ref[index]
                count = 0
                n -= 1
                index = index % n
            else:
                count += 1
                index += 1
                index = index % n
        return ref[0]
