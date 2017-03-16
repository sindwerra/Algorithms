# coding = utf-8

from collections import deque as dq

'''
二叉树的非递归前中后遍历实现
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_ord(root):
    """
    前序遍历迭代实现,用stack
    """
    if root == None: return
    stack = []
    stack.append(root)
    while len(stack):
        node = stack.pop()
        print node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def in_ord(root):
    """
    中序遍历，实现难度比前序高一点
    """
    stack = []
    while root or len(stack):
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print root.val
            root = root.right

def po_ord_double(root):
    """
    后序遍历的双栈实现
    """
    if root == None: return
    ip, opt = [root], []
    while len(ip):
        node = ip.pop()
        opt.append(node)
        if node.left:
            ip.append(ip.left)
        if node.right:
            ip.append(ip.right)

    while len(opt):
        print opt.pop().val

def po_ord_single(root):
    """
    后序遍历的单栈实现，逻辑难度上基本跟红黑树有的一拼...
    """
    if root == None: return
    stack, h, c = stack[root], root, None
    while len(stack):
        c = stack[-1]
        if c.left and c.left <> h and c.right <> h:
            stack.append(c.left)
        elif c.right and c.right <> h:
            stack.append(c.right)
        else:
            print stack.pop().val
            h = c

def lvl_ord_double(root):
    """
    层序遍历的双队列实现，可以一排排的打印node
    这里用stack实现的，不是标准方式，不过速度更快
    """
    if root == None: return
    cur, nxt = dq([root]), dq([])
    while len(cur):
        node = cur.pop()
        if node:
            print node.val
            if node.left:
                nxt.appendleft(node.left)
            if node.right:
                nxt.appendleft(node.right)
        if len(cur) == 0:
            print '\n'
            cur, nxt = nxt, cur

def lvl_ord_single(root):
    """
    单队列层序遍历,用两个变量标记当前层以及下层的数,
    原理其实跟双队列一样，不过把另一个队列换成了两个数来做
    """
    if root == None: return
    cur_num, nxt_num = 1, 0
    store = dq([root])
    while len(store):
        node = store.pop()
        print node.val
        cur_num -= 1
        if node.left:
            store.appendleft(node.left)
            nxt_num += 1
        if node.right:
            store.appendleft(node.right)
            nxt_num += 1
        if cur_num == 0:
            cur_num, nxt_num = nxt_num, cur_num
            print '\n'
