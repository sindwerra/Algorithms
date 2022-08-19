# coding=utf-8

'''
Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary search
tree can be serialized to a string and this string can be deserialized
to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
'''

'''
Binary Tree都可以用的,BST肯定也能用，感觉上好像也不会有更快的方法了
Beat 97.67%
公司：Amazon
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        stack, res = [root], ''
        while stack:
            node = stack.pop()
            if node:
                tmp = str(node.val) + '!'
                stack.append(node.right)
                stack.append(node.left)
            else:
                tmp = '#!'
            res += tmp
        return res[:-1]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        store = data.split('!')
        dummy = TreeNode('3')
        tmp = dummy
        flag = True
        stack = []

        for s in store:
            if s != '#':
                node = TreeNode(s)
                stack.append(node)
                if flag:
                    tmp.left = node
                else:
                    tmp.right = node
                    flag = True
                tmp = node
            else:
                if stack:
                    tmp = stack.pop()
                else:
                    break
                flag = False
        return dummy.left



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
