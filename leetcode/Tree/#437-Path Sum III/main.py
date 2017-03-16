# coding=utf-8

'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in
the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

'''
因为此题的path sum可以不是头尾，所以理论上必须所有的path都要检查一遍
相当于需要O(n^2)的时间复杂度，不过看submission可能有O(n)的方法
Beat 45.26%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, target, tmp, lst):
        if not root:
            return
        if tmp == target:
            lst[0] += 1
        if root.left:
            self.helper(root.left, target, tmp + root.left.val, lst)
        if root.right:
            self.helper(root.right, target, tmp + root.right.val, lst)


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        stack = []
        res = [0]
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                self.helper(root, sum, root.val, res)
                root = root.right
        return res[0]
        
