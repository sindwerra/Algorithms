# coding=utf-8

'''
Given a binary search tree and a node in it,
find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
'''

'''
这题肯定有比变成数组更快的递归遍历方法，待拓展，Beat 18.16%

公司：Pocket Gems， Microsoft， Facebook
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        res = []
        count, index = 0, 0
        while root or len(stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if root == p:
                    index = count
                res.append(root)
                root = root.right
        return res[index] if index < count else None
        
'''
这里就是O(h)的方法，一个节点有右子树的话，直接找右子树的最小值就是后继
没有右子树则从头搜索此节点p，每次向左的选择都用stack记录下来，到达p跳出
此时stack里最上面一个节点即为p的后继，如果stack为空则没有后继
Beat 85%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None

        if p.right:
            return self.treeMin(p.right)

        stack = []
        cur = root
        while cur:
            if cur == p:
                break
            if cur.val > p.val:
                stack.append(cur)
                cur = cur.left
            else:
                cur = cur.right
            
        return stack[-1] if stack else None

    def treeMin(self, root):
        while root.left:
            root = root.left
        return root