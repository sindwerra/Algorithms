# coding=utf-8

'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

'''
一道比较简单的DFS题，因为本题不需要查重，所以少了很多重复性的考虑，只需要根据字典对应的字母列表逐个深搜就搞定了
Beat 68.06%
公司：Amazon, Dropbox, Google, Uber, Facebook
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        store = {'1': ['*'], '2': ['a', 'b', 'c'], 
                '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
                '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'], 
                '8': ['t', 'u', 'v'], '0': [' '],
                '9': ['w', 'x', 'y', 'z']}

        tmp, result = '', []
        self.DFS(0, len(digits), digits, store, tmp, result)
        return result

    def DFS(self, start, end, digits, store, tmp, result):
        if start == end:
            ref = tmp[:]
            result.append(ref)
            return 

        for char in store[digits[start]]:
            self.DFS(start + 1, end, digits, store, tmp + char, result)
                
