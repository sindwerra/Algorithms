# coding=utf-8

'''
题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''

# 就是双指针变长扫整个数组就行
# 设定范围上因为单个数的和在此题不算序列所以只用算到目标数的一半即可

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        tmp = [x for x in xrange(tsum / 2 + 2)]   # 这里改成tsum的话返回值就是res[:-1]
        st, ed = 1, 1
        while ed <= (tsum / 2 + 2):
            ref = sum(tmp[st:ed + 1])
            if ref > tsum:
                st += 1
            elif ref < tsum:
                ed += 1
            else:
                res.append(tmp[st:ed + 1])
                st += 1
                ed += 1
        return res if tsum <> 1 else []
