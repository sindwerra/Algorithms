# coding=utf-8

'''
在XxY的方格中，以左上角格子为起点，右下角格子为终点，
每次只能向下走或者向右走，请问一共有多少种不同的走法
给定两个正整数int x,int y，请返回走法数目。
保证x＋y小于等于12。
测试样例：
2,2
返回：2
'''

'''
排列组合的问题，比如以例子来说就是C21的组合
'''

class Robot:
    def countWays(self, x, y):
        # write code here
        count = x + y - 2
        he = 1
        x -= 1
        y -= 1
        while count:
            he *= count
            count -= 1
        while x > 1:
            he /= x
            x -= 1
        while y > 1:
            he /= y
            y -= 1
        return he
