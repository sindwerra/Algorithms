# coding=utf-8

'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

'''
傻婊子，强行要排个序
'''

# -*- coding:utf-8 -*-
class Solution:
    def PM(self, st, ed, lst, ref):
        if st == ed:
            tmp = ''.join(ref[:])
            if tmp in lst: return
            lst.append(tmp)
            return
        for i in xrange(st, ed):
            ref[i], ref[st] = ref[st], ref[i]
            self.PM(st + 1, ed, lst, ref)
            ref[i], ref[st] = ref[st], ref[i]

    def Permutation(self, ss):
        # write code here
        if ss == '': return []
        res, ref = [], list(ss)
        self.PM(0, len(ref), res, ref)
        res.sort()
        return res
