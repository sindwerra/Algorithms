# coding=utf-8

'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right
corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''

'''
纯反向思维题，找相交的情况太难，但是不相交的情况只有四种很容易看出来
最后找的面积是两个矩形面积覆盖之和，则当四种不相交情况出现时，只要把两个矩形面积相加就可以了
当相交时，则按照如下代码找出重合部分的面积，再用总面积减去重合面积就可以了
Beat 67.88%
'''

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        he = (C - A) * (D - B) + (G - E) * (H - F)
        if C < E or A > G or B > H or D < F:
            return he
        ichi, ni, san, yon = max(A, E), max(B, F), min(C, G), min(D, H)
        return he - (san - ichi) * (yon - ni)
