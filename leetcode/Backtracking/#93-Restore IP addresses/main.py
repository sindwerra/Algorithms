# coding=utf-8

'''
Given a string containing only digits, restore it by returning all possible 
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

'''
和palindrome partition的题基本是一样的，只是要注意分词只能而且必须分成四段，每一段
都必须保持数字在0到255之间，且每一段都不能有leading 0
Beat 1.94% 速度太慢
'''

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        tmp, res = [], []
        self.helper(0, len(s), tmp, res, s, 0)
        return res

    def helper(self, start, end, tmp, res, string, count):
        if count > 4:
            return 

        if start == end:
            if count == 4:
                ref = '.'.join(tmp)
                res.append(ref)
            return 


        for i in xrange(start, end):
            if count < 4 and self.valid(string[start : i + 1]):
                tmp.append(string[start : i + 1])
                self.helper(i + 1, end, tmp, res, string, count + 1)
                tmp.pop()

    def valid(self, string):
        if int(string) > 255:
            return False
        a = len(string.lstrip('0'))
        b = len(string)
        if (a == 0 and b == 1) or a == b:
            return True
        return False