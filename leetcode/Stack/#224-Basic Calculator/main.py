# coding=utf-8

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''

'''
CS32的一道作业题，利用两个stack（operand和operator）
分别保存运算符（包括括号）和数字就行
Beat 40.69%
公司：Google
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip()
        operand, operator = [], []
        st, ed = 0, len(s) - 1
        while st <= ed:
            if s[st] == ' ':
                st += 1
                continue
            elif s[st].isdigit():
                num = 0
                while st <= ed and s[st].isdigit():
                    num = num * 10 + int(s[st])
                    st += 1
                operand.append(num)
                continue
            elif s[st] in ['-', '+', '(']:
                operator.append(s[st])
            else:
                tmp = 0
                while operator[-1] != '(':
                    node = operand.pop()
                    sign = operator.pop()
                    if sign == '-':
                        tmp += (-1 * int(node))
                    else:
                        tmp += int(node)
                tmp += int(operand.pop())
                operator.pop()
                operand.append(tmp)
            st += 1

        res = 0
        while operator:
            node = operand.pop()
            sign = operator.pop()
            if sign == '-':
                res += (-1 * int(node))
            else:
                res += int(node)
        res += int(operand.pop())
        return res
