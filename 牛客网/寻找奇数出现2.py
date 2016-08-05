# coding=utf-8

# leetcode上有一个非常复杂的case过不了

# '''
# 给定一个整型数组arr，其中有两个数出现了奇数次，其他的数都出现了偶数次，找到这两个数。
# 要求时间复杂度为O(N)，额外空间复杂度为O(1)。
# 给定一个整形数组arr及它的大小n，请返回一个数组，其中两个元素为两个出现了奇数次的元素,
# 请将他们按从小到大排列。
# 测试样例：
# [1,2,4,4,2,1,3,5],8
# 返回：[3,5]
# '''

def findOdds(arr, n):
        # write code here
        combine = 0
        for a in arr:
            combine ^= a

        string = bin(combine)
        index = 0
        for b in xrange(len(string)):
            if string[-b - 1] == '1':
                index = b
                break

        one = 0
        for c in arr:
            if len(bin(c)) < index + 3: continue
            if bin(c)[-index - 1] == '1':
               one ^= c

        return [one, combine ^ one] if one < combine ^ one else [combine ^ one, one]
