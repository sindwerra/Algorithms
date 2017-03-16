# coding=utf-8
# KMP算法的伪代码以及Python实现

'''
KMP-matcher(T, P)
    n, m = T.length, P.length
    pi = compute-prefix(P)
    q = 0
    for i = 1 to n
        while q > 0 and T[i] ≠ P[q + 1]
            q = pi[q]
        if T[i] == P[q + 1]
            q += 1
        if q == m
            print 'Hit ' + i - m
            q = pi[q]

compute-prefix(P)
    m = P.length
    pi = [1 .... m]
    pi[1] = 0
    k = 0
    for q = 2 to m
        while k > 0 and P[q] ≠ P[k + 1]
            k = pi[k]
        if P[k + 1] == P[q]
            k += 1
        pi[q] = k
    return pi
'''

def KMP(T, P):
    n, m = len(T), len(P)
    T = ' ' + T
    P = ' ' + P
    pi = compute_prefix(P)
    q = 0
    for i in xrange(1, n + 1):
        while q > 0 and T[i] <> P[q + 1]:
            q = pi[q]
        if T[i] == P[q + 1]:
            q += 1
        if q == m:
            print 'Hit %d' % (i - m)
            q = pi[q]

def compute_prefix(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in xrange(2, m):
        while k > 0 and P[k + 1] <> P[q]:
            k = pi[k]
        if P[k + 1] == P[q]:
            k += 1
        pi[q] = k
    return pi

KMP('bacbababaabcbab', 'ab')
