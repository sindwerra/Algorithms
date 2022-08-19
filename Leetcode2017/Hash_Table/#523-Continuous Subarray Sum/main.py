# coding=utf-8

'''
Given a list of non-negative numbers and a target integer k, write a function to check if 
the array has a continuous subarray of size at least 2 that sums up to the multiple of k, 
that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''

'''
这里是一种O(n^2)的做法，还是先用prefix sum然后逐个检查有没有整除的subarray
这种做法坑多，而且比较慢，LeetCode上还有一种只要O(n)的算法
Beat 25.00%
公司: Facebook
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False

        tmp = [0] * (n + 1)
        for i in xrange(n + 1):
            tmp[i] = tmp[i - 1] + nums[i - 1] if i - 1 >= 0 else 0
            if k == 0:
                if tmp[i] == 0 and i > 1:
                    return True
                continue
            
            if tmp[i] % k == 0 and i > 1:
                return True
        
        for i in xrange(1, n):
            for j in xrange(i + 1, n + 1):
                if k == 0:
                    if tmp[j] - tmp[i - 1] == 0:
                        return True
                    continue
                
                if (tmp[j] - tmp[i - 1]) % k == 0:
                    return True

        return False

'''
O(n)的做法，利用了哈希表，prefix sum的数组不是存和，而是存和膜k之后的值，
这种情况代码需要考虑k等于0的情况，多写一行if在求prefix sum数组时就行了
答案的java代码把prefix sum数组省略了，代码精简很多，但是hashmap里面加了
一行不太好理解0， -1键值对用来处理k等于0的情况，个人不喜欢这样写
Beat 42.40%
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if not n:
            return False

        tmp = [0] * n
        tmp[0] = nums[0] % k if k != 0 else nums[0]
        for i in xrange(1, n):
            if k == 0:
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
                continue
            tmp[i] = (tmp[i - 1] + nums[i]) % k
        
        if k == 0:
            return False
            
        store = {}
        for i in xrange(n):
            if tmp[i] % k == 0 and i >= 1:
                return True
            
            if tmp[i] in store:
                for index in store[tmp[i]]:
                    if abs(index - i) >= 2:
                        return True
            
            if tmp[i] in store:
                store[tmp[i]].append(i)
            else:
                store[tmp[i]] = [i]

        return False