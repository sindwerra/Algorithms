# coding=utf-8

'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight
without alerting the police.
'''

# 解决了中国人民的历史遗留问题啊。。。 半年了终于想出来了，动归正式算入了个门
# Beat 18.66% 速度有点慢啊
# 现在一般写的都是自下而上解，其实可能自上而下解会快一些，虽然代码要复杂一点而且用的是递归

 class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        res = [0] * (n + 1)        # res里面存储的实际上是已有房子到目前长度情况下的最佳偷法获得的钱
        res[1] = nums[0]

        # 当前房子的最优解必然是之前一个房子的最优解和之前两个位置的最优解加上本身价值的最大值
        # 且之前两个格子的最优解是不可能和房子之间无法相邻的原则冲突的，原因的话照动归原则画
        # 个小的最优子结构图就能解释了

        for s in xrange(2, n + 1):
            res[s] = max(nums[s - 1] + res[s - 2], res[s - 1])
        return res[n]
