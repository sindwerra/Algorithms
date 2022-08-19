# coding=utf-8

'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''

'''
这种有重复元素的搜索没有办法做到O(lgn)了，考虑[1,1,1,3,1]和[1,1,3,1,1,1,1,1]
这种case，前中后三数相等是没有办法判断应该往哪边缩小区间的，只能遍历
Beat 69.56%
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        st, ed = 0, len(nums) - 1
        while st <= ed:
            mid = (st + ed) / 2
            if nums[mid] == target:
                return True
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
                    return True
                elif target == nums[ed]:
                    return True
                else:
                    return False
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
                    return True
                elif target == nums[ed]:
                    return True
                else:
                    return False
        return False
