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

    def __partition(self, lst, st, ed):
        """
        :传统快速排序，O(nlgn)
        :type lst: List
        :type st: int
        :type ed: int
        :rtype: int
        """
        
        if st >= ed: return ed
        
        pivot, last = lst[ed], ed
        
        while st <= ed - 1:
            while st <= ed - 1 and lst[st] < pivot: st += 1
            while ed >= st and lst[ed] >= pivot: ed -= 1
            if ed >= st: lst[ed], lst[st] = lst[st], lst[ed]
            
        if lst[st] >= pivot: lst[st], lst[last] = lst[last], lst[st]
        
        return st
    
    def __randomized_partition(self, lst, st, ed):
        """
        :随机划分函数，效果优化
        """
        if ed <= st: return ed
        sign = random.randint(st, ed)
        lst[sign], lst[ed] = lst[ed], lst[sign]
        return self.__partition(lst, st, ed)
        
    def Classical_QS(self, lst, st, ed):
        """
        :传统快速排序主函数, O(nlgn)
        :type lst: List
        :type st: int
        :type ed: int
        :None return 
        """
        
        if st < ed:
            bound = self.__partition(lst, st, ed)
            bound = self.__randomized_partition(lst, st, ed)
            self.Classical_QS(lst, st, bound - 1)
            self.Classical_QS(lst, bound + 1, ed)

    def Python_QS(self, lst):
        """
        :Pythonic快速排序，平均时间复杂度O(nlgn)
        :type lst: List
        :rtyep: List
        """
        if len(lst) <= 1: return lst
        else:
            pivot = lst[0]
            return self.Python_QS([x for x in lst[1 : ] if x < pivot]) + \
                [pivot] + self.Python_QS([x for x in lst[1:] if x >= pivot])

    def counting_sort(self, lst):
        """
        :计数排序，平均时间复杂度O(mn)
        :type lst: List
        :rtype: List
        """
        temp = [0] * max(lst)
        result = [0] * n

        for a in lst:
            temp[a] += 1

        for b in xrange(1, len(temp)):
            temp[b] += temp[b - 1]

        for c in xrange(len(lst) - 1, -1, -1):
            result[temp[lst[c]] - 1] = lst[c]
            temp[lst[c]] -= 1

        return result
