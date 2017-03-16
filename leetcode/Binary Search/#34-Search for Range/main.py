# coding=utf-8

'''
Given a sorted array of integers, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

# 这个题主要想清楚mid定位完之后怎么处理st 和 ed两个点的情况就好
# Beat 74.97%

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        st, ed = 0, len(nums) - 1
        flag = False
        while st <= ed:
            mid = (st + ed) / 2
            if nums[mid] < target:
                st = mid + 1
            elif nums[mid] > target:
                ed = mid - 1
            else:
                flag = True   # 找到了点立即跳出
                break


        if flag != True:      # 没找到点出循环了
            return [-1, -1]
        else:                 # 找到点出循环了
            while st < mid:
                if nums[st] == nums[mid]:
                    break
                st += 1
            while ed > mid:
                if nums[ed] == nums[mid]:
                    break
                ed -= 1
        return [st, ed]


'''
更加干净的版本，但是速度差一点
'''

class Solution(object):
    def searchRange(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        st, ed = 0, len(A) - 1
        mid = 0
        while st <= ed:
            mid = st + (ed - st) / 2
            if A[mid] == target:
                break
            elif A[mid] > target:
                ed = mid - 1
            else:
                st = mid + 1
        if not A or A[mid] != target:
            return [-1, -1]
        else:
            st, ed = mid - 1, mid + 1
            while 0 <= st <= len(A) - 1 and A[st] == target:
                st -= 1
            while 0 <= ed <= len(A) - 1 and A[ed] == target:
                ed += 1
            return [st + 1, ed - 1]
