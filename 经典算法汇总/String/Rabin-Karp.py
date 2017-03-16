# coding=utf-8

'''
Rabin-Karp(T, P, d, q)
    n, m = len(T), len(P)
    h = d^(m - 1) % q
    t = 0
    p = 0
    for i = 1 to m
        t = (dt + T[i]) % q
        p = (dp + P[i]) % q
    for s = 0 to n - m
        if p == t
            if P == T[s ... s + m]
                print 'Hit'
        if s < n - m
            t = (d(t - T[s + 1] * h) + T[s + m + 1]) % q
'''

'''
简化Python版本的Rabin-Karp
'''

def search(txt, pattern, q):
    """
    d等于256，相当于所有的char数量
    """
    n, m = len(txt), len(pattern)
    p, t = 0, 0
    d = 256
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(txt[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if pattern == txt[i:i + m]:
                print 'Here'
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if t < 0:
                t += q

search("GEEKS FOR GEEKS", "GEEK", 101)
