# 买股票的子问题，把find_max_subarray拿出来就行，速度还是慢....

class Solution(object):
    def find_max_crossing_subarray(self, lst, low, mid, high):
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

    def find_max_subarray(self, lst, lo, hi):
        # result = []
        if hi <= lo:
            # result = []
            # result.append(lo)
            # result.append(hi)
            # result.append(lst[lo])
            return lst[lo]
        mid = lo + (hi - lo) / 2
        left = self.find_max_subarray(lst, lo, mid)
        right = self.find_max_subarray(lst, mid + 1, hi)
        cro = self.find_max_crossing_subarray(lst, lo, mid, hi)

        if left >= right and left >= cro:
            # result.append(lo)
            # result.append(hi)
            # result.append(lst[lo])
            return left
        elif right >= left and right >= cro:
            return right
        else: return cro

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_max_subarray(nums, 0, len(nums) - 1)
