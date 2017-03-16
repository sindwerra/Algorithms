# coding=utf-8

'''
实现一个栈的逆序，但是只能用递归函数和这个栈本身的pop操作来实现，而不能自己申请另外的数据结构。
给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。
测试样例：
[4,3,2,1],4
返回：[1,2,3,4]
'''

'''
一个辅助函数找到栈底元素，利用这个函数递归逆序栈排列
'''

# -*- coding:utf-8 -*-

class StackReverse:
    def get(self, stack):
        node = stack.pop()
        if not stack:
            return node
        else:
            last = self.get(stack)
            stack.append(node)
            return last

    def reverseStack(self, A, n):
        # write code here
        if not n: return []
        else:
            node = self.get(A)
            self.reverseStack(A, n - 1)
            A.append(node)
            return A
            
