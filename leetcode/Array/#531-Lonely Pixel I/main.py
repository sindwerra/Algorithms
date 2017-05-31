# coding=utf-8

'''
Given a picture consisting of black and white pixels, find the number of 
black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', 
which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific 
position where the same row and same column don't have any other 
black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
'''

'''
这里是用的counter直接行列比对做的，用DFS做标记也可以
'''

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        n = len(picture)
        if not n:
            return 0
        
        m = len(picture[0])
        if not m:
            return 0
        
        row, col = collections.Counter(), collections.Counter()
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        
        result = 0
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == 'B':
                    if row[i] != 1:
                        continue
                    if col[j] != 1:
                        continue
                    result += 1
        
        return result