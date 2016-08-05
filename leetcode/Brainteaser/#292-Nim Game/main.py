# coding=utf-8

'''
You are playing the following Nim Game with your friend: There is a
heap of stones on the table, each time one of you take turns to remove
1 to 3 stones. The one who removes the last stone will be the winner.
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the
number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win
the game: no matter 1, 2, or 3 stones you remove, the last stone will
always be removed by your friend.

Hint:

If there are 5 stones in the heap, could you figure out a way to remove
the stones such that you will always be the winner?
'''

# 规律就是能整除4的数先手必输

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 第一种返回方式，速度最慢，只比10%的人快

        # if n % 4 == 0: return False
        # return True

        # 第二种返回方式，比43%的人快

        # return n % 4 != 0

        # 第三种返回方式，比65%的人快

        return True if n % 4 != 0 else False
        
