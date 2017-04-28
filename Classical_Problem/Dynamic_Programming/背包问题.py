# coding=utf-8

'''
一个背包有一定的承重cap，有N件物品，每件都有自己的价值，记录在数组v中，
也都有自己的重量，记录在数组w中，每件物品只能选择要装入背包还是不装入背包，
要求在不超过背包承重的前提下，选出物品的总价值最大。
给定物品的重量w价值v及物品数n和承重cap。请返回最大总价值。
测试样例：
[1,2,3],[1,2,3],3,6
返回：6
'''

# 经典01背包问题，CLRS里面也介绍过了，解题思路还是跟找零钱一样，因为有两个
# 变量，所以需要矩阵作为参考结构，具体到单个点res[row][col]，col代表
# 当前能用的最大重量，row到0代表当前允许拿的所有物品，所以res[row][col]
# 只有可能出现两种情况，一种是col本身值小于w[row]，则只可能不拿当前物品
# 一种是col大于w[row]，则此时一种是可以选择不拿此物品即res[row - 1][col]的值，
# 另一种是拿此物品，即res[row - 1][col - w[row]]的值（当前目标重量减去当前物品重量
# 的最优解）加上v[row]的值，二者取最大即可，最后结果就是矩阵右下角的值

class Backpack:
    def maxValue(self, w, v, n, cap):
        # write code here
        res = [([0] * (cap + 1)) for _ in xrange(n)]
        for a in xrange(cap + 1):
            if a >= w[0]:
                res[0][a] = v[0]
        for row in xrange(1，n):
            for col in xrange(1，cap + 1):
                if col >= w[row]:
                    res[row][col] = max(res[row - 1][col], res[row - 1][col - w[row]] + v[row])
                else:
                    res[row][col] = res[row - 1][col]
        return res[n - 1][cap]
