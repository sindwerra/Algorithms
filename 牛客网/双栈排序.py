# coding=utf-8

'''
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个
额外的栈存放临时数据，但不得将元素复制到别的数据结构中。
给定一个int[] numbers(C++中为vector<int>)，其中第一个元素为栈顶，请返回排序后的栈。
请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。
测试样例：
[1,2,3,4,5]
返回：[5,4,3,2,1]
'''

'''
按照视频描述利用一个辅助栈加上一个临时变量进行排序,此处进行的是逆序排序
每次从numbers中弹出栈顶到临时变量上，当变量大于等于辅助栈栈顶时，压入辅助栈，
辅助栈为空时，临时变量压入辅助栈，当临时变量小于栈顶时，一直弹出辅助栈栈顶直到临时变量
大于辅助栈栈顶为止，最后将辅助栈的元素全部压回numbers即可
'''

# -*- coding:utf-8 -*-
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        if not numbers: return []
        stack, cur = [], None
        while numbers:
            cur = numbers.pop()
            if not stack:
                stack.append(cur)
            elif cur >= stack[-1]:
                stack.append(cur)
            else:
                while stack and cur < stack[-1]:
                    numbers.append(stack.pop())
                numbers.append(cur)

        while stack:
            numbers.append(stack.pop())
        return numbers
        
