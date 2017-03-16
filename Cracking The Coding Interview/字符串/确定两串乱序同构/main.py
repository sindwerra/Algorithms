# coding=utf-8

'''
给定两个字符串，请编写程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
这里规定大小写为不同字符，且考虑字符串重点空格。
给定一个string stringA和一个string stringB，
请返回一个bool，代表两串是否重新排列后可相同。保证两串的长度都小于等于5000。
测试样例：
"This is nowcoder","is This nowcoder"
返回：true
"Here you are","Are you here"
返回：false
'''

'''
字典
'''

# -*- coding:utf-8 -*-
class Same:
    def checkSam(self, stringA, stringB):
        # write code here
        a = {}
        for s in stringA:
            if a.has_key(s):
                a[s] += 1
            else:
                a[s] = 1
        for k in stringB:
            if a.has_key(k):
                a[k] -= 1
                if a[k] < 0:
                    return False
            else:
                return False
        return True
