import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
这里实现的时候一个没有parent指针的BST
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right= = None

class BST(object):
    def __init__(self):
        self.root = None
        print 'U created a null BST'
    
    def recursive_traversal(self, root):
        """
        简单的递归中序遍历
        """

        if root:
            self.recursive_traversal(root.left)
            print root.val
            self.recursive_traversal(root.right)

    def iterative_traversal(self, root):
        """
        利用了栈的迭代中序遍历
        """

        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                print root.val
                root = root.right

    def iterative_traversal_without_stack(self, root):
        """
        Morris 中序遍历
        """
        pre, cur = root, None
        
        while pre:
            cur = pre.left
            if cur:
                while cur.right and cur.right != pre:
                    cur = cur.right
                if not cur.right:
                    cur.right = pre
                    pre = pre.left
                    continue
                else:
                    cur.right = None
            print pre.val
            pre = pre.right

    def search(self, root, target):
        if root == None or target == root.val:
            return root
        if target < root.val:
            self.search(root.left, target)
        else:
            self.search(root.right, target)

    def tree_minimum(self, root):
        while root.left:
            root = root.left
        return root

    def tree_maximum(self, root):
        while root.right:
            root = root.right
        return root

    '''
    一个需要背下来的程序段
    '''

    def delete(self, root, value):
        if not root:
            return None
        
        if root.val < value:
            root.right = self.delete(root.right, value)
        elif root.val > value:
            root.left = self.delete(root.left, value)
        else:
            if not root.left:
                tmp = root.right
                root = None
                return tmp
            elif not root.right:
                tmp = root.left
                root = None
                return tmp
            tmp = self.tree_minimum(root.right)
            root.val = tmp.val
            root.right = self.delete(root.right, root.val)
        return tmp