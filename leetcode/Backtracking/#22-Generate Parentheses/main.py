# coding=utf-8

'''
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

'''
DFS里面的查重是一件很头痛的事，尤其是一维的backtracking类型的题，查重更是花样百出
这里主要是明确计数的重点是两倍n，然后所有合法的序列都是当前左括号数大于等于右括号数
另外最后把结果加进result里面的时候左括号数和右括号数必须一样，利用store在当前调用
函数层查重，当前位置只能出现一次加左括号或者右括号
Beat 28.85%
公司：Google, Uber, Zenefits
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(0, 2 * n, '', res, 0, 0)
        return res

    def helper(self, start, end, tmp, res, left, right):
        if start == end and left == right:
            ref = tmp[:]
            res.append(ref)
            return 
        
        store = {}
        for i in xrange(start, end):
            if left > right and ')' not in store:
                store[')'] = 1
                self.helper(start + 1, end, tmp + ')', res, left, right + 1)
            if '(' not in store:
                store['('] = 1
                self.helper(start + 1, end, tmp + '(', res, left + 1, right)