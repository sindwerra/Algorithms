# coding=utf-8

'''
One way to serialize a binary tree is to use pre-order traversal.
When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to
the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is
a correct preorder traversal serialization of a binary tree.
Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer
or a character '#' representing null pointer.

You may assume that the input format is always valid,
for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''

'''
完整的preorder序列最后一个必须是#号，另外去除这个#号之外的元素必然满足括号序列的规则
利用栈就可以判断了最后
Beat 78.59%
公司：Google
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        store = preorder.split(',')
        stack = []
        last = store.pop()
        if last != '#': return False
        n = len(store)
        st = 0
        while st < n:
            if store[st] == '#':
                if not stack: return False
                stack.pop()
            else:
                stack.append(store[st])
            st += 1
        return not stack
