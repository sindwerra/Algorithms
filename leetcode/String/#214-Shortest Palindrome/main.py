# coding=utf-8

'''
Given a string S, you are allowed to convert it to a palindrome by 
adding characters in front of it. Find and return the shortest palindrome 
you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
'''

'''
这题关键在于看出最短的对称串必然是把起始点也囊括进去的最长子字符串那一段
剥掉之后剩下的那段字串反过来加在最前面，gitbook里面详述原因，找到这个串
的方法自然用马拉车了，但是马拉车里面的p和string都是包括了井号的信息的，
所以必须再把这个最长起始点对称子字符串提取出来，最后处理就很简单了
Beat 58.01%
公司：Pocket Gems, Google
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        string = '#' + '#'.join(s) + '#'
        n = len(string)
        p = [0] * n
        maxBorder, maxCenter = 0, 0
        res = [0, 0]
        for i in range(n):
            if maxBorder > i:
                p[i] = min(p[2 * maxCenter - i], maxBorder - i)
            else:
                p[i] = 1
            while i - p[i] >= 0 and i + p[i] < n and string[i - p[i]] == string[i + p[i]]:
                p[i] += 1
            if maxBorder < p[i] + i:
                maxBorder = p[i] + i
                maxCenter = i
                if p[i] > res[1] - res[0]:
                    res = [maxCenter, maxBorder]
        
        index = 0
        for i in xrange(length, -1, -1):
            if i + 1 - p[i] <= 0:
                index = i
                break
            
        tmp = [x for x in string[ : index + p[index]] if x != '#']
        left = s[len(tmp) : ][::-1]
        return left + s