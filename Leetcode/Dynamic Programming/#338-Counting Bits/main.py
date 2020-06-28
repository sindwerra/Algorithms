# coding=utf-8

'''
Given a non negative integer number num. For every numbers i in
the range 0 ≤ i ≤ num calculate the number of 1's in their binary
representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function
like __builtin_popcount in c++ or in any other language.
Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on.
And try to generate new range from previous.
Or does the odd/even status of the number help you
in calculating the number of 1s?
'''

# 每一个数位的前半数的数和之前数位的所有数相等，后半数位的数在前半数位每个数上加一即可
# 再加上一个中间判断，节省时间
# Beat 79.47%

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0, 1]
        size = 2
        while size <= num:
            module = res[size / 2:]
            res += module
            tmp = len(res)
            if tmp > num:                 # 中间判断
                return res[:num + 1]
            another = [x + 1 for x in module]
            res += another
            size *= 2
        return res[:num + 1]
