# coding=utf-8

'''You are given coins of different denominations and a
total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

# 标准动归算法啊，第一个自己解出来的还有点难度的DP，哈哈哈
# Beat 28.04%

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0] * (amount + 1)
        for s in xrange(1, amount + 1):
            q = 1000000
            for i in coins:        # 只需要在存在的硬币种类中遍历就行了，节省非常多的时间这一步
                if s - i >= 0:
                    q = min(q, res[s - i] + 1)
            res[s] = q

        # 如果给的值无法打散，那这个值减去任何现存币值也不可能被打散（动归基本法）

        return res[amount] if res[amount] <> 1000000 else -1
