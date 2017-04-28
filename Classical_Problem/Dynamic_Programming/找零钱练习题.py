# coding=utf-8

'''
有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim(小于等于1000)代表要找的钱数，
求换钱有多少种方法。
给定数组penny及它的大小(小于等于50)，同时给定一个整数aim，请返回有多少种方法可以凑成aim。
测试样例：
[1,2,4],3,3
返回：2
'''

# 艰难啊。。 这题就在于找出矩阵横竖行的定义应该为什么
# 横行是总共有的货币种类数，竖行则为目标钱数，每个点的值等于不用当前货币到达此目标的值
# 加上用一个此货币到达此目标的值（实际已包括所有可能用到此货币的方法）的和
# 经典的动态规划题

class Exchange:
    def countWays(self, penny, n, aim):
        # write code here
        ref = [([0] * (aim + 1)) for _ in xrange(n)]
        for s in xrange(n):
            ref[s][0] = 1
        for j in xrange(aim + 1):
            if j % penny[0] == 0:
                ref[0][j] = 1
        for row in xrange(1, n):
            for col in xrange(1, aim + 1):
                if col - penny[row] < 0:
                    ref[row][col] = ref[row - 1][col]
                else:
                    ref[row][col] = ref[row - 1][col] + ref[row][col - penny[row]]
        return ref[n - 1][aim]
