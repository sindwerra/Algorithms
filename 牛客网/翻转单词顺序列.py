# coding=utf-8

'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''

# 这种题自己写循环比用python的STL函数效率更高
# 另外注意只有空格的输入

class Solution:
    def ReverseSentence(self, s):
        # write code here
        lst = s.split()
        if len(lst) == 0: return s
        lst.reverse()
        res = ''
        for a in lst:
            res += a + ' '
        return res[:-1]
