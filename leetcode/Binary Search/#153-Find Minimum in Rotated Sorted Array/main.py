# coding=utf-8

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

'''
因为没有重复元素，每次二分搜索mid值必然会在条件小于st值或大于ed值中满足一个
经过多次缩小范围后st和ed只差一格或者完全重合（取决于数组长度奇偶），
这时再比较ed和st值哪个较小就行,Beat 77.71%
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        st, ed = 0, len(nums) - 1
        mid = (ed + 1) / 2

        while mid > st and mid < ed:
            if nums[mid] > nums[ed]:
                st = mid
                mid = (st + ed) / 2
            elif nums[mid] < nums[st]:
                ed = mid
                mid = (st + ed) / 2
            else: return nums[0]

        return min(nums[st] , nums[ed])

'''
牛客网介绍的一种通用方法，有没有重复的数的数组都可以用
中间数小于起始数时，必然最小值在左半边，且有可能就是中间值
中间数大于起始数时，最小值在右半边，中间值不是最小值可以mid + 1
中间值大于起始值小于终点值时，这时是如果是有重复值的数组是无法判断最小值在哪里的
Beat 77.65%
'''

class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """

        st, ed = 0, len(arr) - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if arr[mid] < arr[st]:
                ed = mid
            elif arr[mid] > arr[ed]:
                st = mid + 1
            else:
                return min(arr[st : ed + 1])
        return None

'''
没有重复值的数组找最小值，比上面的只是改了一行
Beat 89.69%
'''

class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """

        st, ed = 0, len(arr) - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if arr[mid] < arr[st]:
                ed = mid
            elif arr[mid] > arr[ed]:
                st = mid + 1
            else:
                return arr[st]
        return None


'''
最简洁鲁棒的代码
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        st, end = 0, n - 1
        while st < end:
            mid = st + (end - st) / 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                st = mid + 1
        return nums[st]