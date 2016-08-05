# coding=utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        for s in range(len(temp) / 2):
            if temp[s] == temp[-s - 1]: continue
            else: return False

        return True
