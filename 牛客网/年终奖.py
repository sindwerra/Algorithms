# coding=utf-8

'''
题目描述

小东所在公司要发年终奖，而小东恰好获得了最高福利，
他要在公司年会上参与一个抽奖游戏，游戏在一个6*6的棋盘上进行，上面放着36个价值不等的礼物，
每个小的棋盘上面放置着一个礼物，他需要从左上角开始游戏，每次只能向下或者向右移动一步，
到达右下角停止，一路上的格子里的礼物小东都能拿到，请设计一个算法使小东拿到价值最高的礼物。
给定一个6*6的矩阵board，其中每个元素为对应格子的礼物价值,左上角为[0,0],
请返回能获得的最大价值，保证每个礼物价值大于100小于1000。
'''

# 比较标准的动态规划，因为贴边左边和上边走的两条路只有一种情况可以达到，所以可以先初始化
# 再利用只能右移或者下移的规则比较从第二行第二列开始的所有格子通过右移的情况大还是下移的情况大
# 动归就完成了

class Bonus:
    def getMost(self, board):
        # write code here
        res = [([0] * 6) for _ in xrange(6)]
        res[0][0] = board[0][0]

        for a in xrange(1, 6):
            res[0][a] = res[0][a - 1] + board[0][a]

        for b in xrange(1, 6):
            res[b][0] = res[b - 1][0] + board[b][0]

        for row in xrange(1, 6):
            for col in xrange(1, 6):
                tmp = max(res[row - 1][col], res[row][col - 1]) + board[row][col]
                res[row][col] = tmp

        return res[5][5]
