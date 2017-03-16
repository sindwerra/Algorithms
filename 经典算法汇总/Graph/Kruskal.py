'''
Kruskal(G, w)
    A = ø
    for v in G.V
        make-set(v)
    sort G.E by w
    for e(u, v) in G.E
        if find-set(u) != find-set(v)
            A += e(u, v)
            union(u, v)
    return A
'''
