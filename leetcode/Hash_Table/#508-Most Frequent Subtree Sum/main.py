# coding=utf-8

'''
Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once,
return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in
the range of 32-bit signed integer.
'''

'''
递归求各路和之后再遍历两遍dict就得到答案
Beat 92.21%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, store):
        node = root.val
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left, store)
        if root.right:
            right = self.helper(root.right, store)
        summation = left + right + node
        if store.has_key(summation):
            store[summation] += 1
        else:
            store[summation] = 1
        return summation

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        store = {}
        self.helper(root, store)
        tmp = -sys.maxint
        for s in store.keys():
            if store[s] > tmp:
                tmp = store[s]

        res = []
        for s in store.keys():
            if store[s] == tmp:
                res.append(s)
        return res
