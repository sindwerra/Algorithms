# coding=utf-8

'''
Given a root node reference of a BST and a key,
delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''

'''
算法教材里二叉树最重要的操作之一，这道题实现难点在于没有父节点信息
唯一的办法只能通过runner technique保存之前遍历的结点，因此带来
很多boundary case的问题，另外找寻后继结点并解链返回的函数也很复杂
Beat 67.87%
公司：Uber
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def FM(self, base, root):
        """
        :type base: 起始结点root的父节点，保证root就是后继结点时可以解链
        :type root: 是base结点的右孩子
        """
        pre, cur = None, root
        while cur.left:
            pre = cur
            cur = cur.left
        if cur == root:             # 如果root就是后继结点
            pre = base
            pre.right = cur.right
            return cur
        if not cur.right:           # 如果后继结点没有右孩子
            pre.left = None
            return cur
        else:                       # 如果后继结点没有左孩子
            pre.left = cur.right
            return cur

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        head, cur = TreeNode('dummy'), root   # dummy node保证单节点也可以正确删除
        pre = head
        pre.right = cur
        while cur:                            # 找寻过程
            if cur.val < key:
                pre = cur
                cur = cur.right
            elif cur.val > key:
                pre = cur
                cur = cur.left
            else:
                break

        if not cur: return root               # 没有key的情况

        if not cur.left and not cur.right:    # 删除点是叶节点
            if pre.left == cur:
                pre.left = None
            else:
                pre.right = None
        elif not cur.left:
            if pre.left == cur:
                pre.left = cur.right
            else:
                pre.right = cur.right
        elif not cur.right:
            if pre.left == cur:
                pre.left = cur.left
            else:
                pre.right = cur.left
        else:                                 # 删除点左右孩子都存在
            node = self.FM(cur, cur.right)
            if pre.left == cur:
                pre.left = node
            else:
                pre.right = node
            node.left = cur.left
            node.right = cur.right
        return head.right
