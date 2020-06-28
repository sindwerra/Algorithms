# coding=utf-8

'''
You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -,
you and your friend take turns to flip two consecutive "++" into "--".
The game ends when a person can no longer make a move and
therefore the other person will be the winner.

Write a function to compute all possible states of the string
after one valid move.

For example, given s = "++++", after one move, it may become
one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
'''

'''
遍历翻一遍就好行了
Beat 20.05%

公司：Google
'''

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for index in xrange(len(s) - 1):
            if s[index:index + 2] == '++':
                res.append(s[:index] + '--' + s[index + 2:])
        return res
