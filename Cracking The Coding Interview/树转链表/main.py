'''
有一个类似结点的数据结构TreeNode，包含了val属性和指向其它结点的指针。
其可以用来表示二叉查找树(其中left指针表示左儿子，right指针表示右儿子)。
请编写一个方法，将二叉查找树转换为一个链表，其中二叉查找树的数据结构用TreeNode实现，
链表的数据结构用ListNode实现。
给定二叉查找树的根结点指针root，请返回转换成的链表的头指针。
'''

'''
有了迭代树遍历，这种题太容易了
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Converter:
    def treeToList(self, root):
        # write code here
        stack, dummy = [], ListNode(0)
        cur = dummy
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                cur.next = ListNode(root.val)
                cur = cur.next
                root = root.right
        return dummy.next
