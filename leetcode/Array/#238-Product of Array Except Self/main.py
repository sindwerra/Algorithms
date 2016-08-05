'''
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for
the purpose of space complexity analysis.)
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store = 1
        result = []
        result.append(store)
        for s in range(1, len(nums)):
            store *=  nums[s - 1]
            result.append(store)

        store = 1
        for a in range(len(nums) - 2, -1, -1):
            store *= nums[a + 1]
            result[a] *= store

        return result
