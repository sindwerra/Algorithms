# coding=utf-8

'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree?
Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

'''
跟1基本一样，把tmp的形式从list变成var就符合题目要求了，Beat 44.04%
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None: return None
        cur, nxt = collections.deque([root]), collections.deque([])
        tmp = None
        while len(cur):
            node = cur.pop()
            if tmp:
                tmp.next = node
            tmp = node
            if node.left:
                nxt.appendleft(node.left)
            if node.right:
                nxt.appendleft(node.right)
            if len(cur) == 0:
                tmp = None
                cur, nxt = nxt, cur
        
