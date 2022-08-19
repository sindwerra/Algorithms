# coding=utf-8

'''
Given a non-empty string s and an abbreviation abbr, return whether the string matches 
with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", 
"1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". 
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
'''

'''
标准的模拟算法，主要难点还是corner case太多，首先空字符串是要返回false的
其次缩写的数字起头不能有0，再就是一些长度方面的要求，如最后两个字符串的游标
必须到达最后一个字符之后才行(考虑abcde, a5和hi, hi1的情况)
Beat 98.54%
公司:Google
'''

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not len(word):
            return False
            
        word_cur = 0
        abbr_cur = 0

        while word_cur < len(word) and abbr_cur < len(abbr):
            if abbr[abbr_cur].isdigit():
                if abbr[abbr_cur] == '0':
                    return False
                step = ''
                while abbr_cur < len(abbr) and abbr[abbr_cur].isdigit():
                    step += abbr[abbr_cur]
                    abbr_cur += 1
                word_cur += int(step)
            elif word[word_cur] != abbr[abbr_cur]:
                return False
            else:
                word_cur += 1
                abbr_cur += 1
        
        return True if word_cur == len(word) and abbr_cur == len(abbr) else False