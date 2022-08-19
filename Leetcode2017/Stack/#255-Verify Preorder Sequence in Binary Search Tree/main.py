# coding=utf-8

'''
这里不是O（1）空间的算法
Beat 32.79%
公司：Zenefits
'''

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True
            
        stack = [preorder[0]]
        min = -sys.maxint
        st, ed = 1, len(preorder)

        while st < ed:
            while st < ed and preorder[st] < stack[-1]:
                if preorder[st] < min:
                    return False
                stack.append(preorder[st])
                st += 1
            while stack and st < ed and preorder[st] > stack[-1]:
                tmp = stack.pop()
                min = tmp
            if st < ed:
                stack.append(preorder[st])
            st += 1
        
        return True
