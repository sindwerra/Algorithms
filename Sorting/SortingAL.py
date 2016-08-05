# coding=utf-8

# 造轮子工程第一期

class Mode:
    def __init__(self):
        pass

    def bubble_sort(self, lst, n = None):
        """
        :冒泡排序，时间复杂度O(n^2)
        :type lst: List
        :type n(size of List): int
        :rtype: List
        """
        flag = True

        distance = 0
        if n is None: distance = len(lst)
        else: distance = n


        while flag:
            flag = False
            for index in xrange(distance - 1):
                if lst[index] > lst[index + 1]:
                    lst[index], lst[index + 1] = lst[index + 1], lst[index]
                    flag = True

        return lst

    def selection_sort(self, lst, n = None):
        """
        :选择排序，时间复杂度O(n^2)
        :type lst: List
        :type n(size of List): int
        :rtype: List
        """
        distance = 0
        if n is None: distance = len(lst)
        else: distance = n

        for a in xrange(distance):
            for b in xrange(a + 1, distance):
                if lst[b] < lst[a]:
                    lst[b], lst[a] = lst[a], lst[b]

        return lst

    def insertion_sort(self, lst, n = None):
        """
        :插入排序，时间复杂度O(n^2)
        :type lst: List
        :type n(size of List): int
        :rtype: List
        """
        distance = 0
        if n is None: distance = len(lst)
        else: distance = n

        for a in xrange(1, distance):
            for b in xrange(a, 0, -1):
                if lst[b] < lst[b - 1]:
                    lst[b], lst[b - 1] = lst[b - 1], lst[b]
                else:
                    break

        return lst

    def __merge(self, left, right):
        """
        :归并排序辅助函数
        :type left: List
        :type right: List
        :rtype: List
        """
        l, r = 0, 0
        result = []


        # '''
        # :超过范围剩下的书要一次性压进result中
        # '''


        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        else:
            result += left[l : ]
            result += right[r : ]

        return result

    def merge_sort(self, lst, n):
        """
        :归并排序，平均时间复杂度O(nlgn)
        :type lst: List
        :type n: int
        :rtype: List
        """
        if n <= 1: return lst
        left = self.merge_sort(lst[ : n / 2], n / 2)
        right = self.merge_sort(lst[n / 2 : ], n - n / 2)
        result = self.__merge(left, right)
        return result
