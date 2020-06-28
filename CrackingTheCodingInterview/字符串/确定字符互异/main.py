# -*- coding:utf-8 -*-

# 直觉思维，应该有其他办法更快的

class Different:
    def checkDifferent(self, iniString):
        # write code here
        for a in range(len(iniString)):
            for b in range(a + 1, len(iniString)):
                if iniString[a] == iniString[b]: return False

        return True
