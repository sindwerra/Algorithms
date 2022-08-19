# coding=utf-8

'''
Given a binary tree, find the largest subtree which is a
Binary Search Tree (BST), where largest means subtree with
largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \
 1   8   7
The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.
Hint:

You can recursively use algorithm similar to
98. Validate Binary Search Tree at each node of the tree,
which will result in O(nlogn) time complexity.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
'''

'''
这题要返回四个关键值，一个是此子树是否为BST，一个是此BST有几个点，
一个是BST的最大值，一个BST的最小值，然后后序遍历递归回来之后再判断
本节点是否可以和左右子树一起构成BST，如果可以相应修改返回
如果不行就找左右子树里面结点最多的那颗返回
Beat 85.93%
公司：Microsoft
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root.left and not root.right:
            return [True, 1, root.val, root.val]

        left, right = [True, 0, 'a', 'a'], [True, 0, 'a', 'a']

        if root.left:
            left = self.helper(root.left)
        if root.right:
            right = self.helper(root.right)

        if left[0] and right[0] and left[2] == 'a':
            if root.val < right[3]:
                return [True, right[1] + 1, right[2], root.val]
            else:
                return [False, right[1], right[2], right[3]]
        elif left[0] and right[0] and right[2] == 'a':
            if root.val > left[2]:
                return [True, left[1] + 1, root.val, left[3]]
            else:
                return [False, left[1], left[2], left[3]]
        elif left[0] and right[0] and root.val > left[2] and root.val < right[3]:
            return [True, left[1] + right[1] + 1, right[2], left[3]]
        elif left[1] > right[1]:
            return [False, left[1], left[2], left[3]]
        else:
            return [False, right[1], right[2], right[3]]

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)[1]
