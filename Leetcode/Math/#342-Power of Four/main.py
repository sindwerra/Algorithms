class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 4:
            if num == 1: return True
            else: return False
        elif num % 4 == 0: return self.isPowerOfFour(num / 4)
        else: return False
        
