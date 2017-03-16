# coding=utf-8

'''
Max-cross(lst, st, mid, ed)
    lfp, rtp = 0, 0
    lfs, rts = 0, 0
    sum = 0
    for i = mid to st
        sum += lst[i]
        if sum > lfs
            lfs = sum
            lfp = i

    sum = 0
    for j = mid + 1 to ed
        sum += lst[j]
        if sum > rts
            rts = sum
            rtp = j
    return (lfp, rtp, lfs + rts)

Max-sub(lst, st, ed)
    if st >= ed
        return (st, ed, lst[ed])
    mid = (st + ed) / 2
    lft = Max-sub(lst, st, mid)
    rtt = Max-sub(lst, mid + 1, ed)
    crt = Max-cross(lst, st, mid, ed)
    return max(lft, rtt, crt)
'''
