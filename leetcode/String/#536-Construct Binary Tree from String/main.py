# coding=utf-8

'''
You need to construct a binary tree from a string consisting of parenthesis 
and integers.

The whole input represents a binary tree. It contains an integer followed by 
zero, one or two pairs of parenthesis. The integer represents the root's value 
and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
'''

'''
字符串的处理一定要小心，Divide and Conquer的思路可以很好解决
Beat 46.67%
公司：Amazon
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None

        if s[0] != '(' and s[-1] != ')':
            return TreeNode(int(s))
        
        sign = -1 if s[0] == '-' else 1
        if s[0] == '-':
            s = s[1:]
        res, i = 0, 0
        while i < len(s) and s[i] != '(':
            res = res * 10 + int(s[i])
            i += 1

        head = TreeNode(res * sign)

        tmpString = s[i:]


        stack = 0
        start = 0
        end = len(tmpString)

        while start < end:
            if tmpString[start] == '(':
                stack += 1
            elif tmpString[start] == ')':
                stack -= 1
                if stack == 0:
                    break
            start += 1
        
        left = tmpString[1:start]
        right = None
        if start + 1 < end:
            right = tmpString[start + 2 : end - 1]
        
        head.left = self.str2tree(left)
        head.right = self.str2tree(right)

        return head
