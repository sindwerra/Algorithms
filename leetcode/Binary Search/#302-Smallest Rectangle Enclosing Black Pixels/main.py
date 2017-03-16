# coding=utf-8

'''
An image is represented by a binary matrix with 0 as a white pixel and 1 as a
black pixel. The black pixels are connected, i.e., there is only one black
region. Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels, return the area of the
smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
'''

'''
四个二分就可以了，每一个中间点都要遍历一整行或者一整列，时间复杂度是O(nlgn)
照道理讲BFS也是可以做的
Beat 89.13%
公司：Google
'''

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        row = len(image)
        if not row:
            return 0

        col = len(image[0])
        if not col:
            return 0

        row_st, col_st = 0, 0

        lf_cn, rt_cn, up_cn, bt_cn = y, y + 1, x, x + 1

        end = y
        while col_st <= end:
            mid = col_st + (end - col_st) / 2
            flag = False

            for i in xrange(row):
                if image[i][mid] == '1':
                    flag = True
                    break

            if flag:
                lf_cn = mid
                end = mid - 1
            else:
                col_st = mid + 1

            flag = False

        col_st, end = y, col - 1
        while col_st <= end:
            mid = col_st + (end - col_st) / 2
            flag = False

            for i in xrange(row):
                if image[i][mid] == '1':
                    flag = True
                    break

            if flag:
                rt_cn = mid + 1
                col_st = mid + 1
            else:
                end = mid - 1

            flag = False

        end = x
        while row_st <= end:
            mid = row_st + (end - row_st) / 2
            flag = False

            for i in xrange(col):
                if image[mid][i] == '1':
                    flag = True
                    break

            if flag:
                up_cn = mid
                end = mid - 1
            else:
                row_st = mid + 1

            flag = False

        row_st, end = x, row - 1
        while row_st <= end:
            mid = row_st + (end - row_st) / 2
            flag = False

            for i in xrange(col):
                if image[mid][i] == '1':
                    flag = True
                    break

            if flag:
                bt_cn = mid + 1
                row_st = mid + 1
            else:
                end = mid - 1

            flag = False

        return (rt_cn - lf_cn) * (bt_cn - up_cn)
