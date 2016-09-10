# coding=utf-8

# 百钱百🐔问题

def One_dollar_one_chicken():
    """
    :x, y, z分别代表公鸡，母鸡，鸡雏的个数
    :公鸡5块，母鸡3块，鸡雏3只一块
    """
    result = []
    for x in xrange(101):
        for y in xrange(101 - x):
            z = 100 - x - y
            if z % 3 == 0:
                if 5 * x + 3 * y + z / 3 == 100:
                    result.append((x, y, z))

    return result

# print One_dollar_one_chicken()

# 熄灯问题

class Light_close(object):
    def __init__(self, puzzle):
        self.press = [ [0] * 8 ] * 6
        self.puzzle = puzzle

    def __guess_helper(self):
        """
        :puzzle表示初始输入矩阵，为5*6矩阵
        """

        # 根据press第一行和puzzle数组，计算press其他行的值

        for row in xrange(1, 5):
            for col in xrange(1, 7):
                self.press[row + 1][col] = (self.puzzle[row][col] + self.press[row][col] + \
                            self.press[row - 1][col] + self.press[row][col - 1] + \
                            self.press[row][col + 1]) % 2

        # 判断所计算的press数组能否熄灭第五行的所有灯

        for col in xrange(1, 7):
            if (self.press[5][col - 1] + self.press[5][col] + self.press[5][col + 1] + self.press[4][col]) % 2 != self.puzzle[5][col]:
                return False

        return True

    def enumerate(self):
        """
        :枚举第一行64种情况的辅助函数
        """

        while self.__guess_helper() == False:
            self.press[1][1] += 1
            col = 1
            while self.press[1][col] > 1:    # 遍历第一行64种情况，累加进位
                self.press[1][col] = 0
                col += 1
                self.press[1][col] += 1


if __name__ == '__main__':
    print One_dollar_one_chicken()
    case_one = [
                [0,0,0,0,0,0,0,0],
                [0,0,1,1,0,1,0,0],
                [0,1,0,0,1,1,1,0],
                [0,0,0,1,0,0,1,0],
                [0,1,0,0,1,0,1,0],
                [0,0,1,1,1,0,0,0]
                ]
    # test = Light_close(case_one)
    # print test
    # print test.puzzle
    # print test.press
    # test.enumerate()
    # print test.press
