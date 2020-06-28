class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.strip()
        if temp == '': return 0
        lst = temp.split()
        last = lst[len(lst) - 1]
        return len(last)
