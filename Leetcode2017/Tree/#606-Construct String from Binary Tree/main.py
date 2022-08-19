# coding=utf-8

'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder 
traversing way.

The null node needs to be represented by empty parenthesis pair "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship 
between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between 
the input and the output.
'''

'''
理解它的case就好
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root:
            return ''
            
        if not root.left and not root.right:
            return str(root.val)

        head = str(root.val)
        left = self.tree2str(root.left)
        if root.right:
            right = self.tree2str(root.right)
            return head + '(' + left + ')' + '(' + right + ')'
        return head + '(' + left + ')'