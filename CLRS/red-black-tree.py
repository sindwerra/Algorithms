class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'

class Solution:
    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            if x.key != 0:
                print 'key:', x.key, 'parent:', x.parent.key, 'color:', x.color
            self.InorderTreeWalk(x.right)

    def LeftRotate(self, T, x):
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def RBInsert(self, T, z):
        # init z
        z.left = T.nil
        z.right = T.nil
        z.parent = T.nil

        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = 'red'
        self.RBInsertFixup(T,z)

    def RBInsertFixup(self, T, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.LeftRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.RightRotate(T,z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.LeftRotate(T, z.parent.parent)
        T.root.color = 'black'

    def RBTransplant(self, T, u, v):
        if u.parent == T.nil:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBDelete(self, T, z):
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.RBTransplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.RBTransplant(T, z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(T, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(T, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.RBDeleteFixup(T, x)

    def RBDeleteFixup(self, T, x):
        while x != T.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.LeftRotate(T, x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.RightRotate(T, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.LeftRotate(T, x.parent)
                    x = T.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.RightRotate(T, x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.LeftRotate(T, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.RightRotate(T, x.parent)
                    x = T.root
        x.color = 'black'

    def TreeMinimum(self, x):
        while x.left != T.nil:
            x = x.left
        return x

nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
s = Solution()
for node in nodes:
    s.RBInsert(T,RBTreeNode(node))

s.InorderTreeWalk(T.root)

s.RBDelete(T,T.root)
print 'after delete'
s.InorderTreeWalk(T.root)
