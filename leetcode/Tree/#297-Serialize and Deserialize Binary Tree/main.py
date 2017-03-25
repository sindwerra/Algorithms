# coding=utf-8

'''
Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or
memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ
serializes a binary tree. You do not necessarily need to follow
this format, so please be creative and come up with different
approaches yourself.
Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
'''

'''
序列化需要将空叶子节点也考虑进来，只有将所有#考虑才能分辨不同结构的树
反序列化则可以先创立一个dummy node来进行树重构，利用flag变量可以判断前一个结点是否
为空节点，如果为空则利用存储了node的stack栈来弹出之前存在的结点并将指向从左变为右
序列化的具体方法则是每个结点的值转为string型变量并加一个！号，如果是空节点加#号
最后通过拆解此string变量来重构树结构
此题用前序，中序，后序，层级遍历皆可做
Beat 79.03%
公司：Linkedin, Google, Uber, Facebook, Amazon, Microsoft, Yahoo, Bloomberg
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''                # 空树情况
        stack, res = [root], ''
        while stack:
            node = stack.pop()                # 前序遍历的变体，不论
            if node:                          # 左右孩子是否为空皆纳入
                tmp = str(node.val) + '!'
                stack.append(node.right)
                stack.append(node.left)
            else:
                tmp = '#!'
            res += tmp

        # Python split函数的原因，最后一个!号必须去掉

        return res[:-1]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        store = data.split('!')           # 拆分输入string变量
        dummy = TreeNode('3')             # dummy node避免判断初始情况
        tmp = dummy                       # 移动指针tmp来定位新node的位置
        flag = True                       # flag变量用来判定是否方向转右
        stack = []                        # 存储新建node的stack

        for s in store:
            if s != '#':
                node = TreeNode(s)
                stack.append(node)        # 保存node到栈里备用
                if flag:                  # 当前s是tmp的左孩子
                    tmp.left = node
                else:
                    tmp.right = node      # 当前s不是tmp的左孩子，是tmp的右孩子
                    flag = True           # tmp指向从新变为默认左方向
                tmp = node                # 更新tmp指针
            else:
                if stack:
                    tmp = stack.pop()     # 当前节点为空跳回上一个非空节点
                else:
                    break                 # stack中已无非空节点，跳出循环
                flag = False              # 默认方向左向已无结点
        return dummy.left


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


'''
这里是BFS算法的序列化，其实想出来之后再看的确比前中后序遍历的算法好理解多了
Beat 97.58%
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        res = ''
        
        while q:
            node = q.pop()
            if node:
                res += (str(node.val) + '!')
                q.appendleft(node.left)
                q.appendleft(node.right)
            else:
                res += '#!'
                continue
            
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split('!')
        tmp = []
        n = len(lst)
        
        for node in lst:
            if node == '#':
                tmp.append(None)
            else:
                tmp.append(TreeNode(node))
        
        offset = 0
        
        for i in xrange(n):
            if not tmp[i]:
                offset += 2
                continue
            left = 2 * i + 1 - offset
            right = 2 * i + 2 - offset
            if left < n:
                tmp[i].left = tmp[left]
            if right < n:
                tmp[i].right = tmp[right]
        
        return tmp[0]