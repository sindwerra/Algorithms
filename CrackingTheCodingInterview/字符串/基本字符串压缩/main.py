# coding=utf-8

'''
利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。
比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。若压缩后的字符串没有变短，
则返回原先的字符串。
给定一个string iniString为待压缩的串(长度小于等于10000)，
保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。
测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr"
'''

'''
没有难度
'''

# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        cur, count = iniString[0], 0
        res = ''
        for s in iniString:
            if s == cur:
                count += 1
            else:
                res += (cur + str(count))
                cur = s
                count = 1
        res += (cur + str(count))
        return res if len(res) < len(iniString) else iniString
