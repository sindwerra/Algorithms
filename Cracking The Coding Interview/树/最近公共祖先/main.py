'''
有一棵无穷大的满二叉树，其结点按根结点一层一层地从左往右依次编号，根结点编号为1。
现在有两个结点a，b。请设计一个算法，求出a和b点的最近公共祖先的编号。
给定两个int a,b。为给定结点的编号。请返回a和b的最近公共祖先的编号。
注意这里结点本身也可认为是其祖先。
测试样例：
2，3
返回：1
'''

'''
第一种方法比较笨，用较大数建数组然后上溯，过程中所有经过的下标元素变为1
再用较小数上溯找公共祖先
'''

# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        da, xiao = max(a, b), min(a, b)
        ref = [0] * (da + 1)
        while da:
            ref[da] = 1
            da /= 2
        while xiao:
            if ref[xiao] == 1:
                return xiao
            xiao /= 2
        return None

'''
第二种思路，有点像求最大公约数的方法，a大a除以2，b大b除以2，最后终会相等
'''

# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        while a != b:
            if a > b:
                a /= 2
            else:
                b /= 2
        return a
