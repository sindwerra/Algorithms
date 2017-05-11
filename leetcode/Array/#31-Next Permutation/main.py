# coding=utf-8

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater 
permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order 
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs 
are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

'''
此题也算是疑难杂症之一了，基本没什么算法，就是发现这个规律就好了，照着geeksforgeeks上面讲的
找最右的一个当前元素比下一个元素小的位置，如果没有这样的位置直接翻转整个数组，找到这个位置后再
从这个位置往右找跟它差值最小的数的位置，找到这个位置后把两数互换，最后再把原位置往右的所有元素
翻转一遍就是要求的next permutation了，基本没什么规律，非要证明只能通过permutation那个逻辑
去证明了
Beat 90.11%
公司：Google
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        st, ed = 0, n - 1
        flag = False
        
        for i in xrange(ed, 0, -1):
            if nums[i] > nums[i - 1] and not flag:
                pos = self.find(nums, nums[i - 1], i, ed)
                nums[i - 1], nums[pos] = nums[pos], nums[i - 1]
                self.reverse(nums, i, ed)
                flag = True
        
        if not flag:
            nums.reverse()
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def find(self, nums, base, start_pos, end_pos):
        result = None
        compare = sys.maxint
        
        for i in xrange(start_pos, end_pos + 1):
            if nums[i] - base > 0:
                if nums[i] - base < compare:
                    result = i
        
        return result