class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        str = str.strip()      # 剥掉两边多余的空
        i = 0
        n = 0
        pos = True             # 判断正负数flag

# 有正负号的话跳过第一格，负号修改pos值

        if str[0] == '+' or str[0] == '-':
            i = 1
            if str[0] == '-': pos = False

# C语言教材中看到的代码

        while i < len(str) and ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
                n = 10 * n + ord(str[i]) - ord('0')      # 从高位转换string为int的方法
                i += 1

# 64位机没有32位的最大值常数设定，只能手动写判断条件，若为32位机可以直接用sys.maxint

        if pos:
            if n >= 2 ** 31: return 2 ** 31 - 1
            return n

        else:
            if n >= 2 ** 31: return -(2 ** 31)
            return -1 * n
