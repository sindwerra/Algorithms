# coding=utf-8

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators 
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''

'''
逻辑太脏了
公司：Airbnb
Beat 56.58%
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operand = collections.deque([])
        opeartor = collections.deque([])
        lst = list(s.strip())
        n = len(lst)
        i = 0

        while i < n:
            if lst[i] != ' ':
                if lst[i].isdigit():
                    base = 0
                    while i < n and lst[i].isdigit():
                        base = 10 * base + int(lst[i])
                        i += 1
                    operand.append(base)
                elif lst[i] == '+' or lst[i] == '-':
                    opeartor.append(lst[i])
                    i += 1
                elif lst[i] == '*':
                    i += 1
                    while i < n and lst[i] == ' ':
                        i += 1
                    base = 0
                    while i < n and lst[i].isdigit():
                        base = 10 * base + int(lst[i])
                        i += 1
                    operand[-1] *= base
                else:
                    i += 1
                    while i < n and lst[i] == ' ':
                        i += 1
                    base = 0
                    while i < n and lst[i].isdigit():
                        base = 10 * base + int(lst[i])
                        i += 1
                    operand[-1] /= base
            else:
                i += 1
            
        while len(operand) > 1:
            tmp = operand.popleft()
            sign = opeartor.popleft()
            if sign == '+':
                operand[0] = tmp + operand[0]
            else:
                operand[0] = tmp - operand[0]
        
        return operand[-1]