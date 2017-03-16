# coding=utf-8

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。

def jumpFloorII(number):
    # write code here
    res = [0] * (number + 1)
    for s in xrange(1, number + 1):
        q = 0
        for i in xrange(s):
            q += res[i]
        res[s] = q + 1   # 之前所有1到n-1的方法全加起来之后再加一就是最优解规模了
    return res[number]
