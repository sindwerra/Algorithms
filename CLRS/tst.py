import sys
from sets import Set

# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         n = len(nums)
#         self.store = [[0 for a in xrange(n)] for b in xrange(n)]
#         # print self.store
#         for s in xrange(n):
#             self.store[s][s] = nums[s]
#         # print self.store
#
#         for row in xrange(n):
#             for col in xrange(row + 1, n):
#                 print type(self.store)
#                 print type(self.store[row])
#                 print type(self.store[row][col])
#                 print type(nums[row][col])
#                 self.store[row][col] = self.store[row][col - 1] + nums[row][col]
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return self.store[i][j]
#
# nums = [-2,0,3,-5,2,-1]
#
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)


# def FindNumbersWithSum(array, tsum):
#         # write code here
#         if len(array) <= 1: return []
#         res = [sys.maxint, sys.maxint]
#         st, ed = 0, len(array) - 1
#         while st < ed:
#         	# if array[ed] + array[st] > tsum:
#             #     ed -= 1
#             # elif array[ed] + array[st] < tsum:
#             #     st += 1
#             # else:
#             #     if array[ed] * array[st] < res[0] * res[1]:
#             #         res[0] = array[st]
#             #         res[1] = array[ed]
#             #     st += 1
#             #     ed -= 1
#             if array[ed] + array[st] > tsum:
#                 ed -= 1
#             elif array[ed] + array[st] < tsum:
#                 st += 1
#             else:
#                 if array[ed] * array[st] < res[0] * res[1]:
#                     res[0] = array[st]
#                     res[1] = array[ed]
#                 st += 1
#                 ed -= 1
#         return res
#
# print FindNumbersWithSum([1,2,2,3,5,7,8],9)
# print FindNumbersWithSum([1,1,2],3)
# print FindNumbersWithSum([1],1)
# print FindNumbersWithSum([1,2],3)

# def FindContinuousSequence(tsum):
#         # write code here
#         res = []
#         tmp = [x for x in xrange(tsum + 1)]
#         st, ed = 1, 1
#         while ed <= (tsum + 1):
#             ref = sum(tmp[st:ed + 1])
#             if ref > tsum:
#                 st += 1
#             elif ref < tsum:
#                 ed += 1
#             else:
#                 res.append(tmp[st:ed + 1])
#                 st += 1
#                 ed += 1
#         return res
#
# print FindContinuousSequence(100)

# class NumMatrix(object):
#     def __init__(self, matrix):
#         """
#         initialize your data structure here.
#         :type matrix: List[List[int]]
#         """
#         row = len(matrix)
#         if row == 0: return
#         col = len(matrix[0])
#         if col == 0: return
#
#         self.store = [([0] * (col + 1)) for _ in xrange(row + 1)]
#         self.ref = matrix
#
#         for i in xrange(row):
#             for j in xrange(col):
#                 self.store[i][j] = matrix[i][j]
#
#         for r in xrange(row):
#             for c in xrange(col):
#                 # self.store[r][c] += self.store[r][c - 1]
#                 if c != 0:
#                     self.store[r][c] += (self.store[r][c - 1] + matrix[r][c])
#                 else:
#                     self.store[r][c] = matrix[r][c]
#
#     def sumRegion(self, row1, col1, row2, col2):
#         """
#         sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
#         res = 0
#         for s in xrange(row1, row2 + 1):
#             res += (self.store[s][col2] - self.store[s][col1] + self.ref[s][col1])
#             # print self.store[s][col2]
#             # print self.store[s][col1]
#             # print self.ref[s][col1]
#         return res
#
# matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# numMatrix = NumMatrix(matrix)
# print numMatrix.sumRegion(2, 1, 4, 3)
# print numMatrix.sumRegion(1, 1, 2, 2)
# print numMatrix.sumRegion(1,2,2,4)


# def maxValue(w, v, n, cap):
#         # write code here
#         res = [0] * (cap + 1)
#
#         for s in xrange(n):
#             w[s] = [w[s], v[s]]
#
#         w.sort()
#
#         for i in xrange(1, cap + 1):
#             q = 0
#             for j in w:
#                 if i - j[0] < 0:
#                     break
#                 else:
#                     q = max(q, res[i - j[0]] + j[1])
#             res[i] = q
#             print 'This is %d round: value is %d' % (i, q)
#         return res[cap]
#
# lst = [42,25,30,35,42,21,26,28]
# another=[261,247,419,133,391,456,374,591]
# print maxValue(lst, another, 8, 297)

# def calcMonoSum(A, n):
#         # write code here
#         res = [0] * n
#         for i in xrange(1, n):
#             if A[i] >= A[i - 1]:
#                 res[i] = res[i - 1] + A[i - 1]
#                 print res[i]
#             else:
#                 for j in xrange(i - 1, -1, -1):
#                     if A[j] <= A[i]:
#                         res[i] = res[j] + A[j]
#
#         print res
#         return sum(res)
#
# print calcMonoSum([1,3,5,2,4,6],6)

# def threeSum(nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         res = []
#         st, ed = 0, len(nums) - 1
#         cur = ed - 1
#         while st < ed - 1:
#             cp = nums[st] + nums[ed]
#             cur = ed - 1
#             tmp = []
#             flag = False
#             while cur > st:
#                 if nums[cur] + cp < 0:
#                     break
#                 elif nums[cur] + cp > 0:
#                     cur -= 1
#                 else:
#                     tmp.append(nums[st])
#                     tmp.append(nums[cur])
#                     tmp.append(nums[ed])
#                     flag = True
#                     break
#             if flag == False:
#                 st += 1
#             else:
#                 res.append(tmp)
#                 ed -= 1
#         return res
#
# print threeSum([-1,0,1,2,-1,-4])
# print threeSum([0,0,0,0])

# def countWays(penny, n, aim):
#         # write code here
#         ref = [([0] * (aim + 1)) for _ in xrange(n)]
#         for s in xrange(n):
#             ref[s][0] = 1
#         for j in xrange(aim + 1):
#             if j % penny[0] == 0:
#                 ref[0][j] = 1
#         for row in xrange(1, n):
#             for col in xrange(1, aim + 1):
#                 if col - penny[row] < 0:
#                     ref[row][col] = ref[row - 1][col]
#                 else:
#                     ref[row][col] = ref[row - 1][col] + ref[row][col - penny[row]]
#         print ref
#         return ref[n - 1][aim]
#
# print countWays([1,2,4],3,3)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def in_order(root, lst):
#         if root == None:
#             return
#         in_order(root.left, lst)
#         lst.append(root.val)
#         in_order(root.right, lst)
#
# def chkIdentical(A, B):
#     # write code here
#     lst_A, lst_B = [], []
#     in_order(A, lst_A)
#     in_order(B, lst_B)
#     n, m = len(lst_A), len(lst_B)
#     # print lst_A
#     # print lst_B
#     for s in xrange(n - m + 1):
#         print lst_A[s:s+m]
#         if lst_A[s:s + m] == lst_B:
#             return True
#     return False
#
# a=TreeNode(1)
# b=TreeNode(2)
# c=TreeNode(3)
# d=TreeNode(4)
# e=TreeNode(5)
# f=TreeNode(6)
# g=TreeNode(7)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# c.left=f
# c.right=g
#
# h=TreeNode(1)
#
# print chkIdentical(a, h)
#
# def KMP(T, P):
#     n, m = len(T), len(P)
#     pi = compute_pre(P)
#     q = -1
#     for i in xrange(n):
#         while q > 0 and P[q + 1] != T[i]:
#             print '1'
#             q = pi[q]
#         if P[q + 1] == T[i]:
#             q += 1
#         if q == m:
#             print 'Pattern match on %d' % (i - m)
#             q = pi[q]
#
# def compute_pre(P):
#     m = len(P)
#     pi = [0] * m
#     k = -1
#     for q in xrange(1, m):
#         while k > 0 and P[k + 1] != P[q]:
#             k = pi[k]
#         if P[k + 1] == P[q]:
#             k += 1
#         pi[q] = k
#     return pi
#
# # KMP('bacbababaabcbab', 'ababaca')
# print compute_pre('ababaca')
