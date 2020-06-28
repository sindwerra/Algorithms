# coding=utf-8

# '''
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary
# as 00000010100101000001111010011100), return 964176192 (represented
# in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
# '''

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        cha = 34 - len(bin(n))               # 补齐32位码
        store = cha * '0' + bin(n)[2:]       # 拼装
        return int(store[::-1], 2)           
