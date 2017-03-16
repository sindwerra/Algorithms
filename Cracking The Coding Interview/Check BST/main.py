'''
中序遍历转成list再判断
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Checker:
    def checkBST(self, root):
        # write code here
        stack, res = [], []
        count = 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
                count += 1
        for s in range(count - 1):
            if res[s] > res[s + 1]:
                return False
        return True
