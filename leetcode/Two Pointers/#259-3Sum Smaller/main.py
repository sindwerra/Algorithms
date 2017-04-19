# coding=utf-8

'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k 
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
'''

'''
思路还是跟3Sum基本一样，不过这里重复的数也可以算进来，另外不用每个都去遍历
st + ed的数小于零时就可以直接用下标算了，不用所有都遍历一次
Beat 64.75%
公司：Google
'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        base = 0
        res = 0

        while base <= n - 3:
            a = nums[base]
            st, ed = base + 1, n - 1
            while st <= ed - 1:
                b, c = nums[st], nums[ed]
                if a + b + c < target:
                    res += (ed - st)
                    st += 1
                else:
                    ed -= 1
            base += 1
        
        return res