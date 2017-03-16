# coding=utf-8

'''
Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array
return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

'''
General的情况有六种，高的部分左边多或者高的部分左边少
再加上正常没有rotate过的情况，以及短数组的情况（1个数或者2个数）
Beat 77.32%
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st, ed = 0, len(nums) - 1
        while st <= ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if target < nums[st] and target < nums[ed]:
                    if nums[mid] < nums[ed]:
                        ed = mid - 1
                    else:
                        st = mid + 1
                elif target > nums[st] and target > nums[ed]:
                    ed = mid - 1
                elif target > nums[st] and target < nums[ed]:
                    ed = mid - 1
                elif target == nums[st]:
                    return st
                elif target == nums[ed]:
                    return ed
                else:
                    return -1
            else:
                if target > nums[st] and target > nums[ed]:
                    if nums[mid] > nums[ed]:
                        st = mid + 1
                    else:
                        ed = mid - 1
                elif target < nums[st] and target < nums[ed]:
                    st = mid + 1
                elif target > nums[st] and target < nums[ed]:
                    st = mid + 1
                elif target == nums[st]:
                    return st
                elif target == nums[ed]:
                    return ed
                else:
                    return -1
        return -1

'''
逻辑简化过的版本，这种旋转情况一定要先检查st, ed, mid三个数是否和target相等
再进行区间缩小，因为区间缩小代价太大，需要尽量避免
Beat 65.67%
'''

class Solution(object):
    def search(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st, ed = 0, len(A) - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if target == A[st]:
                return st
            if target == A[ed]:
                return ed
            if A[mid] == target:
                return mid
            elif target < A[mid]:
                if A[mid] > A[ed] and target < A[ed]:
                    st = mid + 1
                else:
                    ed = mid - 1
            else:
                if A[mid] < A[ed] and target > A[ed]:
                    ed = mid - 1
                else:
                    st = mid + 1
        return -1
