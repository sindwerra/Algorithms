import operator

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = {}
        result = []
        for s in nums:
            if temp.has_key(s):
                temp[s] += 1
            else:
                temp[s] = 1

        # 下面这行用了operator库里面的itemgetter函数，1代表用value排序，
        # 0表示用key排序，返回值是一个element为tuple的list
        # 此为python中为依照key或者value给dict排序的最优方法


        sorted_x = sorted(temp.items(), key=operator.itemgetter(1))

        for a in range(k):
            result.append(sorted_x[-a - 1][0])

        result.sort()

        return result
