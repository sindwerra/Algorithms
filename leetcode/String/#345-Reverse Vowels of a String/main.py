class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = list(s)
        store = []
        result = []

        for a in range(len(temp)):
            if temp[a] in 'AEIOUaeiou':
                store.append(temp[a])
                temp[a] = 'what'

        for b in range(len(temp)):
            if temp[b] == 'what':
                result.append(store.pop())
            else: result.append(temp[b])

        result = ''.join(result)
        return result


# Leetcode里python list里面的iterator和index遍历无法在loop里面改变元素的值
# 只能重新建新list
# split函数只能把有空格的多个词组成的句子分割切片成每个词为元素组成的list
