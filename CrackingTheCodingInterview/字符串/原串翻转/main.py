# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        # write code here
        result = ''

        for s in range(len(iniString) - 1, -1, -1):
            result += iniString[s]

        return result
