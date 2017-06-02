# coding=utf-8

'''
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden.
 Your job is to fence the entire garden using the minimum length of rope as it is expensive. 
 The garden is well fenced only if all the trees are enclosed. Your task is to help find the 
 coordinates of trees which are exactly located on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will 
separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
'''

'''
惊不惊喜，意不意外
公司：Google
'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        n = len(points)
        if n < 3:
            return points

        start = 0
        for i in xrange(1, n):
            if points[start].x > points[i].x:
                start = i
        
        res = set([])
        cur, nxt = start, -1
        while True:
            nxt = (cur + 1) % n
            res.add(points[cur])
            for i in xrange(n):
                if self.orientation(points[cur], points[nxt], points[i]) == 1:
                    nxt = i
            
            for i in xrange(n):
                if i != nxt and i != cur:
                    if self.inBetween(points[cur], points[nxt], points[i]) and self.orientation(points[cur], points[nxt], points[i]) == 0:
                        res.add(points[i])

            cur = nxt
            if cur == start:
                break
        
        return list(res)

    def orientation(self, A, B, C):
        result = (B.y - A.y) * (C.x - B.x) - (C.y - B.y) * (B.x - A.x)
        if not result:
            return 0
        
        return 1 if result > 0 else 2
        
    def inBetween(self, A, B, C):
        if C.x <= max(A.x, B.x) and C.x >= min(A.x, B.x) and C.y <= max(A.y, B.y) and C.y >= min(A.y, B.y):
            return True
        return False