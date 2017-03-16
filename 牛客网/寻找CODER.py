# coding=utf-8

'''
请设计一个高效算法，再给定的字符串数组中，找到包含"Coder"的字符串(不区分大小写)，
并将其作为一个新的数组返回。结果字符串的顺序按照"Coder"出现的次数递减排列，
若两个串中"Coder"出现的次数相同，则保持他们在原数组中的位置关系。
给定一个字符串数组A和它的大小n，请返回结果数组。保证原数组大小小于等于300,其中每个串的
长度小于等于200。同时保证一定存在包含coder的字符串。
测试样例：
["i am a coder","Coder Coder","Code"],3
返回：["Coder Coder","i am a coder"]
'''

# 因为需要同长串保持相对稳定，最好的办法就是计数排序的思路做

class Coder:
    def findCoder(self, A, n):
        # write code here
        tmp = [[] for _ in xrange(40)]
        res = []
        nor = 'coder'
        for string in A:
            tmp[string.lower().count(nor) - 1].append(string)

        for index in xrange(39, -1, -1):
            while len(tmp[index]) <> 0:
                res.append(tmp[index].pop(0))
        return res
