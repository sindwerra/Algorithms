# coding=utf-8

'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

'''
逻辑完全没难度，主要是一个考虑带符号数，还有一些Python语言本身的坑，比如
1. 负数字符串isdigit函数判断不出来是数字字符串
2. -5/90 或者 5/-90之类是等于-1不是数学中的0
公司：LinkedIn
Beat 82.55%
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if (token[0] == '-' or token[0] == '+') and token[1:].isdigit():
                stack.append(int(token))
                continue
            if token.isdigit():
                stack.append(int(token))
                continue
            tmp = stack.pop()
            if token == '+':
                stack[-1] += tmp
            elif token == '-':
                stack[-1] -= tmp
            elif token == '/':
                if not stack[-1]:
                    continue
                A = abs(stack[-1])
                B = abs(tmp)
                stack[-1] = (A / B) * (A / stack[-1]) * (B / tmp)
            else:
                stack[-1] *= tmp

            
        return stack[0]
            