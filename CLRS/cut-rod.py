# coding=utf-8

# 切钢条问题的迭代解

# def cut_rod(price, n):
#     """""""""""""""""
#     :切钢条问题动态规划O(n^2)解
#     :price type: list
#     :n type: integer
#     """""""""""""""""
#     res = [0] * (n + 1)
#     for i in xrange(1, n + 1):
#         q = -30000             # 此值只是为了代替python最小值
#         for j in xrange(1, i + 1):
#             q = max(q, price[j] + res[i - j])
#         res[i] = q
#     return res[n]


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print cut_rod(price, 10)
