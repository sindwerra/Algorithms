# coding=utf-8

'''有一个只由0，1，2三种元素构成的整数数组，
请使用交换、原地排序而不是使用计数进行排序。
给定一个只含0，1，2的整数数组A及它的大小，
请返回排序后的数组。保证数组大小小于等于500。
测试样例：
[0,1,1,0,2,2],6
返回：[0,0,1,1,2,2]'''

# 快排双指针思维

def sortingThreeColor(A, n):
    lf, cur, rt = 0, 0, n - 1
    while cur <= rt:
        if A[cur] == 1:
            cur += 1
        elif A[cur] == 0:
            A[cur], A[lf] = A[lf], A[cur]
            cur += 1
            lf += 1
        else:
            A[cur], A[rt] = A[rt], A[cur]
            rt -= 1
    return A
