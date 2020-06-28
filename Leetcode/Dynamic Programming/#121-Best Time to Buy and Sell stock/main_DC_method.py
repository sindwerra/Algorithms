
# 根据教材写的标准算法，用中心点将数组两部分平分开并以中心点为基准去判断左右分数组最大值
# 算法本身不是很坚固，当mid和high两个参数相等时，右半部分的循环不会运行，返回值变成
# 负无限大了，不过因为本身只是一个辅助函数，它的缺陷被调用它的find_max_subarray函数
# 掩盖了。另外根据leetcode，运行速度是非常慢的
# 函数本身的返回值可以是一个包含了这个最大值以及其数组的起始点和终止点值的数组也可以仅仅是
# 这个最大值本身，取决于需要可以改变

def find_max_crossing_subarray(lst, low, mid, high):
    left_sum = float('-inf')
    left_point = 0
    sum = 0
    for s in range(mid, low - 1, -1):
        sum += lst[s]
        if float(sum) > left_sum:
            left_sum = sum
            left_point = s

    right_sum = float('-inf')
    right_point = 0
    sum = 0
    for a in range(mid + 1, high + 1):
        sum += lst[a]
        if float(sum) > right_sum:
            right_sum = sum
            right_point = a

    result = []
    result.append(left_point)
    result.append(right_point)
    result.append(left_sum + right_sum)
    return result[2]

# 通过mid点和mid + 1参数避免了find_max_crossing_subarray中的mid和high参数相等
# 将纯左分数组的最大值和纯右分数组的最大值以及跨越数组的最大值进行比较，返回其中的最大值
# 实际上本质是通过Divide Conquer将数组无限细分，最后所有的结果都是通过find_max_crossing_subarray
# 这个函数来处理的

def find_max_subarray(lst, lo, hi):
    # result = []
    if hi <= lo:
        # result = []
        # result.append(lo)
        # result.append(hi)
        # result.append(lst[lo])
        return lst[lo]
    mid = lo + (hi - lo) / 2
    left = find_max_subarray(lst, lo, mid)
    right = find_max_subarray(lst, mid + 1, hi)
    cro = find_max_crossing_subarray(lst, lo, mid, hi)

# 此部分可以用max函数实现

    if left >= right and left >= cro:
        # result.append(lo)
        # result.append(hi)
        # result.append(lst[lo])
        return left
    elif right >= left and right >= cro:
        return right
    else: return cro

# 主调用函数通过循环构建一个每日股价和前一天股价差价的数组，这个数组和前面的两个
# 函数合并使用就可以找到股价的最大收益

def maxProfit(prices):
    lst = [0]
    for s in range(1, len(prices)):
        lst.append(prices[s] - prices[s - 1])
    return find_max_subarray(lst, 0, len(prices) - 1)



lst = [6,8,-9,10,0,-5,-4,19,2,-7,-1,1]
# print find_max_crossing_subarray(lst, 2, 3, 3)
# print find_max_crossing_subarray(lst, 0, 0, 0)
print find_max_subarray(lst, 0, 11)
