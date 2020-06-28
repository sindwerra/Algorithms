# coding=utf-8

'''
Given a non-empty array of integers, return the third maximum number
in this array. If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist,
so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means
the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

# 三个临时变量最大，次大，第三大，有一个滚动过程
# 另外最后返回值时考虑是否数组并没有三个不同的数
# Beat 85.99%

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = -sys.maxint - 1, -sys.maxint - 1, -sys.maxint - 1
        for s in nums:
            if s > three:
                one = two
                two = three
                three = s
            elif s > two and s < three:
                one = two
                two = s
            elif s > one and s < two:
                one = s
        return one if one != -sys.maxint - 1 else three
