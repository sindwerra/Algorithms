# coding=utf-8

'''
DFS(G)
    for v in G
        v.pi = nil
        v.c = white
    time = 0
    for v in G
        if v.color = white
            DFS-Visit(G, v)

DFS-Visit(G, v)
    time += 1
    v.d = time
    v.color = gray
    for u in v.adj
        if u.color = white
            u.pi = v
            DFS-Visit(G, u)
    time += 1
    v.f = time
    v.color = black

BFS(G, s)
    for v in G
        v.d = ∞
        v.pi = nil
        v.color = white
    s.d = 0
    s.pi = nil
    s.color = gray
    Q = {}
    enq(Q, s)
    while len(Q) <> 0
        u = deq(Q)
        for v in u.adj
            if v.color = white
                v.d = u.d + 1
                v.color = gray
                v.pi = u
                enq(Q, v)
        u.color = black
'''
