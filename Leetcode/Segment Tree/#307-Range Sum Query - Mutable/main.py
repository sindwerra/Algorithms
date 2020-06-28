# coding=utf-8

'''
Given an integer array nums,
find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating
the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange
function is distributed evenly.
'''

'''
此题用了相当于就是要写一个segment tree的数据结构，并且是用array形式表示的
geeksforgeeks解释了全过程
update和getsum函数必须要写辅助函数
Beat 63.19%
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            self.n = len(nums)
            self.array = nums
            self.store = [0] * (2 * int(2 ** math.ceil(math.log(self.n, 2))) - 1)
            self.construct(self.array, self.store, 0, self.n - 1, 0)

    def construct(self, ip_ar, sgt, start, end, index):
        if start == end:
            sgt[index] = ip_ar[start]
            return sgt[index]

        mid = start + (end - start) / 2
        sgt[index] = self.construct(ip_ar, sgt, start, mid, 2 * index + 1) + self.construct(ip_ar, sgt, mid + 1, end, 2 * index + 2)
        return sgt[index]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if i < 0 or i > self.n - 1:
            return
        diff = val - self.array[i]
        self.array[i] = val
        self.updateUTI(i, 0, self.n - 1, diff, 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeUTI(i, j, 0, self.n - 1, 0)

    def sumRangeUTI(self, qstart, qend, start, end, index):
        if qstart <= start and qend >= end:
            return self.store[index]
        if qstart > end or qend < start:
            return 0

        mid = start + (end - start) / 2
        return self.sumRangeUTI(qstart, qend, start, mid, 2 * index + 1) + self.sumRangeUTI(qstart, qend, mid + 1, end, 2 * index + 2)

    def updateUTI(self, i, start, end, diff, index):
        if start == end:
            self.store[index] += diff
            return
        mid = start + (end - start) / 2
        self.store[index] += diff
        if i <= mid:
            self.updateUTI(i, start, mid, diff, 2 * index + 1)
        else:
            self.updateUTI(i, mid + 1, end, diff, 2 * index + 2)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
