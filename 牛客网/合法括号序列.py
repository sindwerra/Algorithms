# coding=utf-8

# '''
# 对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。
# 给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。
# 测试样例：
# "(()())",6
# 返回：true
# 测试样例：
# "()a()()",7
# 返回：false
# 测试样例：
# "()(()()",7
# 返回：false
# '''

# -*- coding:utf-8 -*-

class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        if n % 2 != 0: return False
        stack = []
        for s in xrange(n - 1, -1, -1):
            if A[s] == ')': stack.append(A[s])
            elif A[s] == '(':
                if stack[-1] == ')': stack.pop()
                else: return False
            else: return False

    	return True
