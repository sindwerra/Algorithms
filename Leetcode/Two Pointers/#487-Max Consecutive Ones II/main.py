# coding=utf-8

'''
Given a binary array, find the maximum number of consecutive 1s in 
this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, 
you can't store all numbers coming from the stream as it's too large to hold in memory. 
Could you solve it efficiently?
'''

'''
这题还是套路型的双指针，一块一慢同向前进，只是有一些复杂的逻辑判断必须注意，如快指针超过之后循环就可以停止了
还有慢指针必须先出发扫到第一个不是0的点为止，最后还需要有一个变量来保存上一段连续1的长度，每次快指针停下
之后就来判断当前这一段连续1加上上一段连续1是不是能拼成一个最长1，另外连续0的情况通过tmp变量的计算实际上
也考虑进去了，最后每个慢指针循环完了之后慢指针并不是往前推一格而是直接跳到当前快指针停下的地方
Beat 97.73%
公司：Google
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, cur = 0, 0
        n = len(nums)
        pre_one = 0
        result = 0

        while start < n and nums[start] == 1:
            pre_one += 1
            start += 1
        
        if start == n:
            return n
        
        cur = start + 1
        while start < n:
            while cur < n and nums[cur] == 1:
                cur += 1

            tmp = cur - start - 1
            if pre_one + tmp + 1 > result:
                result = pre_one + tmp + 1
            pre_one = tmp

            if cur >= n:
                break
            
            start = cur
            cur += 1
        
        return result
                

        