# coding=utf-8

'''
Given a string representing arbitrarily nested ternary expressions, calculate 
the result of the expression. You can always assume that the given expression is 
valid and only consists of digits 0-9, ?, :, T and F (T and F represent 
True and False respectively).

Note:

The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
Example 1:

Input: "T?2:3"

Output: "2"

Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: "F?1:T?4:5"

Output: "4"

Explanation: The conditional expressions group right-to-left. Using parenthesis, 
it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:

Input: "T?T?F:5:3"

Output: "F"

Explanation: The conditional expressions group right-to-left. Using parenthesis, 
it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
'''

'''
stack类型的题，boundary case太多了，而且真心很难事先考虑到啊
公司：Snapchat
Beat 15.30%
'''

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        n = len(expression)
        i = 0
        operator = []

        while i < n:
            if expression[i] == '?':
                operator.append(expression[i])
                i += 1
            elif expression[i] == ':':
                if operator[-1] == ':':
                    false = stack.pop()
                    true = stack.pop()
                    status = stack.pop()
                    if status == 'T':
                        stack.append(true)
                    else:
                        stack.append(false)
                    operator.pop()
                    operator.pop()
                else:
                    operator.append(expression[i])
                    i += 1
            else:
                stack.append(expression[i])
                i += 1
        
        while len(stack) > 1:
            false = stack.pop()
            true = stack.pop()
            status = stack.pop()
            if status == 'T':
                stack.append(true)
            else:
                stack.append(false)
        
        return stack[-1]

