# coding=utf-8

# 有两个从小到大排序以后的数组A和B，
# 其中A的末端有足够的缓冲空容纳B。请编写一个方法，将B合并入A并排序。
# 给定两个有序int数组A和B，A中的缓冲空用0填充，
# 同时给定A和B的真实大小int n和int m，请返回合并后的数组。

def mergeAB(A, B, n, m):
    while m <> 0:
        while n > 0 and A[n - 1] >= B[m - 1]:
            A[n + m - 1] = A[n - 1]
            n -= 1
        if n <= 0:
            for s in xrange(m - 1, -1, -1):
                A[s] = B[s]
            break
        else:
            while m > 0 and B[m - 1] > A[n - 1]:
                A[n + m - 1] = B[m - 1]
                m -= 1
    return A
