# coding=utf-8

'''
n个人站队，他们的编号依次从1到n，要求编号为a的人必须在编号为b的人的左边，
但不要求一定相邻，请问共有多少种排法？第二问如果要求a必须在b的左边，并且一定要相邻，请问一共有多少种排法？
给定人数n及两个人的编号a和b，请返回一个两个元素的数组，其中两个元素依次为两个问题的答案。
保证人数小于等于10。
测试样例：
7,1,2
返回：[2520,720]
'''

'''
两个人不紧邻则在左在右几率一样，除以二就行
紧邻则相当于一个人，求少一个人的组合数就行
'''

# -*- coding:utf-8 -*-

class StandInLine:
    def getWays(self, n, a, b):
        # write code here
        res = []
        cur = n
        sum = 1
        while cur > 1:
            sum *= cur
            cur -= 1
        res.append(sum / 2)
        res.append(sum / n)
        return res
