# coding=utf-8

'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

'''
标准的分治算法思维，可能有其他的方式解决，不过这里参照的是清华数据结构课介绍的思路
第一种思路，最为清晰易理解，但是因为递归调用过多额外内存导致内存超限
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])

        mid = inorder.index(preorder[0])   # 利用preorder的头结点也就是根节点划分数组
        lchild = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        rchild = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        root = TreeNode(preorder[0])
        root.left = lchild
        root.right = rchild
        return root

'''
参考discussion后的第二种方式，由于preorder和inorder数组规模太大导致内存超限
这时观察可以发现每次分治只需要把中序数组分开就行，因为preorder数组永远是按照顺序
从前到后来划分inorder数组的，这样preorder的分数组就不存在了，只需要保存inorder
数组的子数组就行，Beat 51.34%
'''

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0: return None

        node = preorder.pop(0)   # 每次都是preorder的第一个数来划分inorder，需要弹出
        mid = inorder.index(node)
        root = TreeNode(node)
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid + 1:])
        return root
