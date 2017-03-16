# coding=utf-8

'''
Huffman(C)
    n = C.length
    Q = C
    for i = 1 to n - 1
        alloc new node z
        z.left = x = ext-min(Q)
        z.right = y = ext-min(Q)
        z.freq = x.freq + y.freq
        Insert(Q, z)
    return ext-min(Q)
'''
