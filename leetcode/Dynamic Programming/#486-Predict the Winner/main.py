# coding=utf-8

'''
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers 
from either end of the array followed by the player 2 and then player 1 and so on. 
Each time a player picks a number, that number will not be available for the next player. 
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player 
plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, 
then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. 
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True 
representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''

'''
这道题和九章的coins in a line III一样，结合了区间类动归和博弈类动归的一道题，基本上还是套的博弈类的模板
，区间在于每一次取数只有两种情况，一种往左边，一种往右边，但是中间这一段是不会变的，所以参考矩阵应该基于
数组的下标来定义和初始化，这也是区间类动归的一个特点，即初始化的值不是矩阵的边缘而是矩阵中心的某些位置在此题
中，需要初始化的位置是对角线和i + 1 == j的位置，另外i > j的位置都是不需要考虑的位置，因为这样的区间不存在
Beat 98.31%
公司：Google
'''

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if not n:
            return False
        
        res = [([0] * n) for _ in xrange(n)]
        ref = [([False] * n) for _ in xrange(n)]
        
        return 2 * self.helper(0, n - 1, ref, res, nums) >= sum(nums)

    def helper(self, i, j, ref, res, nums):
        if ref[i][j]:
            return res[i][j]
        
        ref[i][j] = True
        if i == j:
            res[i][j] = nums[i]
            return res[i][j]
        elif i + 1 == j:
            res[i][j] = max(nums[i], nums[j])
            return res[i][j]
        elif i > j:
            return res[i][j]
        else:
            a = self.helper(i + 2, j, ref, res, nums)
            b = self.helper(i + 1, j - 1, ref, res, nums)
            c = self.helper(i, j - 2, ref, res, nums)
            res[i][j] = max(min(a, b) + nums[i], min(b, c) + nums[j])
            return res[i][j]