def LIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = [0] * n
        for s in xrange(n):
            q = 0
            for k in xrange(s):
                if nums[k] < nums[s]:
                    q = max(q, res[k])
            res[s] += (q + 1)
        return max(res) if n <> 0 else 0
