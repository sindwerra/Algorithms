# coding=utf-8

'''
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

'''
这种思路是一个list的和不是偶数首先排除，其次如果list里的最大值大于list的和的一半也直接排除
其余的情况则使用dp矩阵自底向上推导，Beat 20.43%，肯定不是最优算法
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ref = sum(nums)
        if ref % 2 == 1: return False
        else:
            tmp = ref / 2
            n = len(nums)
            matrix = [([False] * (tmp + 1)) for _ in xrange(n)]
            for a in xrange(tmp + 1):
                if nums[0] == a:
                    matrix[0][a] = True

            for row in xrange(1, n):
                for col in xrange(1, tmp + 1):
                    if col == nums[row]:
                        matrix[row][col] = True
                    elif col < nums[row]:
                        matrix[row][col] = matrix[row - 1][col]
                    else:
                        matrix[row][col] = (matrix[row - 1][col] | matrix[row - 1][col - nums[row]])
                if matrix[row][tmp]:
                    return True
            return False
