# coding=utf-8

# 双指针头尾同时开始遍历

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = 0
        ed = len(s) - 1
        while st < ed:
            while st <= ed and not s[st].isalpha() and not s[st].isdigit(): st += 1    # st <= ed必须写在前面
            while st <= ed and not s[ed].isalpha() and not s[ed].isdigit(): ed -= 1
            if st >= ed: break
            if s[st].lower() != s[ed].lower(): return False   # 所有string值都可以用于lower函数，不光是字母
            st += 1
            ed -= 1

        return True
