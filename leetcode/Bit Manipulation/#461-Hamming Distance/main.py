# coding=utf-8

'''
The Hamming distance between two integers is the number of
positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits
are different.
'''

'''
太简单，不想说话，Beat 90.81%
公司：Facebook
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a, b = bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)
        count = 0
        for s in range(32):
            if a[s] != b[s]:
                count += 1
        return count
