# coding=utf-8

'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
'''

'''
问题不难，但是逻辑结构太复杂了
关键要知道三点，左子树是否为univalue，右子树是否为univalue，左子树和右子树的
univalue是否一致且和root value一致，另外空树以及叶节点都算univalue，思路基本上
就是判断平衡树的算法改进，但是逻辑判断多太多了
Beat 55.65%

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def CUS(self, root, count):
        if not root: return ('a', True)
        if not root.left and not root.right:
            count[0] += 1
            return (root.val, True)
        a = self.CUS(root.left, count)
        b = self.CUS(root.right, count)
        if a[1] and b[1]:
            if a[0] == b[0] and a[0] == root.val:
                count[0] += 1
                return (root.val, True)
            elif a[0] == 'a' and b[0] == 'a':
                count[0] += 1
                return (root.val, True)
            elif a[0] == 'a':
                if b[0] == root.val:
                    count[0] += 1
                    return (root.val, True)
                else:
                    return (root.val, False)
            elif b[0] == 'a':
                if a[0] == root.val:
                    count[0] += 1
                    return (root.val, True)
                else:
                    return (root.val, False)
            else:
                return (root.val, False)
        else:
            return (root.val, False)

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.CUS(root, res)
        return res[0]
