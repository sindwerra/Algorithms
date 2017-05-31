# coding=utf-8

'''
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." Besides the root, 
each house has one and only one parent house. After a tour, the smart thief 
realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses 
were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

'''

'''
DFS加哈希表记录重复访问搞定
Beat 43.00%
公司：Uber
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        store = {}
        return self.DFS(root, True, store)
    
    def DFS(self, root, status, store):
        if not root:
            return 0
        
        if (root, status) in store:
            return store[(root, status)]

        result = 0
        a = self.DFS(root.left, True, store) + self.DFS(root.right, True, store)
        if status:
            b = root.val + self.DFS(root.left, False, store) + self.DFS(root.right, False, store)
            result = max(a, b)
            store[(root, True)] = result
            return result
        store[(root, False)] = a
        return a