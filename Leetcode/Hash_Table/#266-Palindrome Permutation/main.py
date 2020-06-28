# coding=utf-8

'''
Given a string, determine if a permutation of the string could
form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference
do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
'''

'''
哈希表搞定，Beat 52.06%
公司：Google, Uber, Bloomberg
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = {}
        for a in s:
            if store.has_key(a):
                store[a] += 1
            else:
                store[a] = 1

        odd = 0
        for k in store.keys():
            if store[k] % 2:
                odd += 1
        return odd <= 1
