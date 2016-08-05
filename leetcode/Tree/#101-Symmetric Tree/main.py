''' Given a binary tree, check whether it is a mirror of
itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traversal(self, root, lst, direction):
        if root == None:
            lst.append('x')  # 加X在空node上保证列表的结构完整使判断准确
            return
        lst.append(root.val)
        if direction:
            self.traversal(root.left, lst, direction)
            self.traversal(root.right, lst, direction)
        else:
            self.traversal(root.right, lst, direction)
            self.traversal(root.left, lst, direction)

# 一个优先向左遍历，一个优先向右遍历，这样构成的两个分支list的每个值就相等了

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        zuo = []
        you = []
        if root == None: return True
        self.traversal(root.left, zuo, True)
        self.traversal(root.right, you, False)
        if len(zuo) != len(you): return False
        for s in range(len(zuo)):
            if zuo[s] != you[s]: return False

        return True
