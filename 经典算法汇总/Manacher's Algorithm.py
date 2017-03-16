# coding=utf-8

'''
manacher算法
'''

def manacher(s):
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
    return ''.join([x for x in string[2 * res[0] - res[1] + 1 : res[1]] if x != '#'])
