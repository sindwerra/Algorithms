# coding=utf-8

def determinant(lst, n):
    """""""""""""""""""""""
    :type lst: 一个二维方形矩阵
    :type n: 矩阵的尺寸
    """""""""""""""""""""""

    he = 0
    for std in xrange(n):
        ji = lst[0][std]
        for offset in xrange(1, n):
            ji *= lst[offset][(std + offset) % n]
        he += ji

    cha = 0
    for std in xrange(n - 1, -1, -1):
        ji = lst[0][std]
        for offset in xrange(1, n):
            ji *= lst[offset][(std - offset + n) % n]
        cha += ji

    return he - cha

if __name__ == '__main__':
    matrix_1 = [[1,2,3],[5,8,1],[3,1,2]]
    matrix_2 = [[1,2], [5,8]]
    matrix_3 = [5]
    matrix_4 = [[15,15,213,-5], [3,3,89,-123],[312,334,-1,4],[3,-1,-6,-10]]
    matrix_5 = [[-2,2,-3],[-1,1,3],[2,0,-1]]
    matrix_6 = [[-2,2,-3],[0,2,-4],[0,0,4.5]]
    matrix_7 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix_8 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,12,11],[10,9,8,7,6],[5,4,3,2,1]]
    assert matrix_1[1][1] == 8
    assert determinant(matrix_1, 3) == -56
    # assert determinant(matrix_2, 2) == -2
    # print determinant(matrix_3, 1)
    # assert determinant(matrix_4, 4) == 34231620
    assert determinant(matrix_5, 3) == 18
    assert determinant(matrix_6, 3) == -18
    assert determinant(matrix_7, 4) == 0
    # assert determinant(matrix_8, 5) == 0
    print determinant(matrix_8, 5)
