# coding=utf-8

'''
We define the Perfect Number is a positive integer that is equal to the sum 
of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect 
number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''

'''
从题目条件就能看出来最多也只能用O(n**0.5)级别的算法了，然后就发现在根号n之前就可以截止循环
因为n可以被 一个数整除则意味着也可以被这个整除后得到的结果整除，所以就可以包括大于根号n的数
了，另外注意当前数平方等于n时只能加一遍，而且除以1时只能加1本身,lgn的算法是个纯数学算法
意义不大
Beat 80.33%
公司：Fallible
'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 5:
            return False
            
        result = 0
        
        for i in xrange(1, int(num ** 0.5) + 1):
            if num % i == 0:
                result += i
                if i * i != num and i != 1:
                    result += (num / i)
        
            if result > num:
                return False
                
        return result == num