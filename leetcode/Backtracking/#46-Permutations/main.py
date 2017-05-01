# coding=utf-8

'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

'''
geeksforgeeks上面的题，还是标准回溯算法，Beat 92.60%
'''

class Solution(object):
    def PM(self, st, ed, lst, nums):
        if st == ed:
            tmp = nums[:]
            lst.append(tmp)
            return
        for i in xrange(st, ed):
            nums[i], nums[st] = nums[st], nums[i]
            self.PM(st + 1, ed, lst, nums)
            nums[i], nums[st] = nums[st], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.PM(0, len(nums), res, nums)
        return res

'''
另一种
'''

class Solution(object):
    def GP(self, A, lst, st, ed):
        if st >= ed - 1:
            ref = A[:]
            lst.append(ref)
        else:
            for i in xrange(st, ed):
                A[i], A[st] = A[st], A[i]
                self.GP(A, lst, st + 1, ed)
                A[st], A[i] = A[i], A[st]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.GP(nums, res, 0, len(nums))
        return res


'''
迭代版本
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permuatations = []
        
        if not nums:
            return []
        
        n = len(nums)
        stack = []
        stack.append(-1)

        while stack:
            last = stack.pop()
            nxt = -1

            for i in xrange(last + 1, n):
                if i not in stack:
                    nxt = i
                    break
            
            if nxt == -1:
                continue
            
            stack.append(nxt)
            for i in xrange(n):
                if i not in stack:
                    stack.append(i)
            
            permuatation = []
            for i in xrange(n):
                permuatation.append(nums[stack[i]])
            permuatations.append(permuatation)
        
        return permuatations