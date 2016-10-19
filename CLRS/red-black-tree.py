# coding=utf-8

# CLRS中红黑树的Python实现

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.color = None
        self.parent = None

class Red_Black_Tree(object):
    def __init__(self):
        """""""""
        :构造函数
        :root作为头节点指针
        :dummy作为尾部空节点存在
        """""""""
        self.root = None
        self.dummy = TreeNode(None)
        self.dummy.color = 'Black'

    def insert(self, z):
        """""""""
        :插入函数
        :z type: TreeNode
        """""""""
        x = self.root
        y = self.dummy
        while x != self.dummy:
            y = x
            if x.val < z.val:
                x = x.right
            else:
                x = x.left
        z.parent = y
        if y == self.dummy:
            self.root = z
        elif y.val < z.val:
            y.right = z
        else:
            y.left = z
        z.left = self.dummy
        z.right = self.dummy
        z.color = 'Red'
        self.insert_fix(z)

    def insert_fix(self, z):
        """""""""
        :插入修正函数
        :z type: TreeNode
        """""""""
        while z.parent.color == 'Red':
            if z.parent.parent.left == z.parent:
                y = z.parent.parent.right
                if y.color == 'Red':
                    y.color = 'Black'
                    z.parent.color = 'Black'
                    z.parent.parent.color = 'Red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'Black'
                    z.parent.parent.color = 'Red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'Red':
                    y.color = 'Black'
                    z.parent.color = 'Black'
                    z.parent.parent.color = 'Red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'Black'
                    z.parent.parent.color = 'Red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'Black'

    def delete(self, z):
        """""""""
        :删除函数
        :z type: TreeNode
        """""""""
        y = z
        y_ori_color = z.color
        if z.left == self.dummy:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.dummy:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_min(z.right)    # tree_min函数还没写
            y_ori_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_ori_color == 'Black':
            self.delete_fix(x)

    def delete_fix(self, x):
        """""""""
        :删除修正函数
        :x type: TreeNode
        """""""""
        while self.dummy != x and x.color == 'Black':
            if x.parent.left == x:
                w = x.parent.right
                if w.color == 'Red':
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent
                else:
                    if w.right.color == 'Black':
                        w.left.color = 'Black'
                        w.color = 'Red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    w.right.color = 'Black'
                    x.parent.color = 'Black'
                    self.left_rotate(x.parent)
                    self.root = x
            else:
                w = x.parent.left
                if w.color == 'Red':
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent
                else:
                    if w.left.color == 'Black':
                        w.right.color = 'Black'
                        w.color = 'Red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    w.left.color = 'Black'
                    x.parent.color = 'Black'
                    self.right_rotate(x.parent)
                    self.root = x
        x.color = 'Black'

    def transplant(self, u, v):
        """""""""
        :移植函数
        :u type: TreeNode
        :v type: TreeNode
        """""""""
        if u.parent == self.dummy:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def left_rotate(self, z):
        """""""""
        :左转函数
        :z type: TreeNode
        """""""""
        y = z.right
        z.right = y.left
        if y.left != None:
            y.left.parent = z
        y.parent = z.parent
        if z.parent == self.dummy:
            self.root = y
        elif z.parent.left == z:
            z.parent.left = y
        else:
            z.parent.right = y
        y.left = z
        z.parent = y

if __name__ == '__main__':
    a = Red_Black_Tree()
    # print a.dummy.color
