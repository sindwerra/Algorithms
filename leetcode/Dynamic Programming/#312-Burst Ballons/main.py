class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0

        ref = [([0] * (n + 2)) for _ in xrange(n + 2)]
        flag = [([False] * (n + 2)) for _ in xrange(n + 2)]

        return self.memoiz(nums, 1, n, ref, flag, n)

    def memoiz(self, nums, i, j, ref, flag, n):
        if flag[i][j]:
            return ref[i][j]
        
        flag[i][j] = True
        
        left = nums[i - 2] if i - 2 >= 0 else 1
        right = nums[j] if j < n else 1

        for index in xrange(i, j + 1):
            a = self.memoiz(nums, i, index - 1, ref, flag, n)
            b = self.memoiz(nums, index + 1, j, ref, flag, n)
            ref[i][j] = max(ref[i][j], left * right * nums[index - 1] + a + b)
        return ref[i][j]

