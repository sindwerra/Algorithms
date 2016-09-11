# coding=utf-8

class Heap(object):
    def __init__(self, tpl = None):
        self.store = []
        if tpl != None:
            self.build_max_heap(tpl)
            self.store = tpl[:]

    def __str__(self):
        return 'This is a Heap instance'

    def get_contents(self):
        return self.store

    def __sift_down(self, lst, st, ed):
        """
        :堆排序下沉函数，时间复杂度O(lgn)
        :type lst: List
        :type n: int
        """
        lf, rt = 2 * st + 1, 2 * st + 2     # Left child 和 right child
        lar = st                            # 最大数的坐标，初始值为需要下沉点的坐标
        if lf <= ed and lst[lf] > lst[st]:
            lar = lf
        if rt <= ed and lst[rt] > lst[lar]:
            lar = rt
        if lar != st:
            lst[st], lst[lar] = lst[lar], lst[st]
            self.__sift_down(lst, lar, ed)

    def build_max_heap(self, lst):
        """
        :创建最大堆函数，理论时间复杂度O(nlgn),实际情况一般为O(n)
        :type lst: List
        """
        for s in xrange(len(lst) / 2 - 1, -1, -1):
            self.__sift_down(lst, s, len(lst) - 1)

    def heap_sort(self, lst, n):
        """
        :此函数可以被外部list参数单独用以排序，跟建立的heap实例没有任何联系
        :堆排序，时间复杂度O(nlgn)
        :type lst: List
        :type n: 输入List的长度
        :rtype: 返回排序完成的输入List
        """
        self.build_max_heap(lst)
        for s in xrange(n):
            lst[0], lst[n - s - 1] = lst[n - s - 1], lst[0]
            self.__sift_down(lst, 0, n - s - 2)
        return lst

class Priority_Queue(Heap):
    def __init__(self, lst = None):
        self.store = []
        if lst != None:
            self.build_max_heap(lst)
            self.store = lst

    def heap_maximum(self):
        return self.store[0]

    def heap_extract_max(self):
        if len(self.store) <= 1:
            return 'Error! Heap underflow'
        lar = self.store[0]
        self.store[-1], self.store[0] = self.store[0], self.store[-1]
        self.store.remove(lar)
        
if __name__ == '__main__':
    template1 = [3, 4, 9, -10, 20, 0, 156]
    template2 = [1, 0]
    srt = Heap(template1)
    # print srt.bubble_sort(template1)
    # print srt.bubble_sort(template1, 2)
    # print srt.bubble_sort(template2)
    # print srt.bubble_sort(template2, 2)
    # print srt.selection_sort(template1, 7)
    # print srt.selection_sort(template1)
    # print srt.selection_sort(template2, 2)
    # print srt.selection_sort(template2)
    # print srt.insertion_sort(template1)
    # print srt.insertion_sort(template1, 7)
    # print srt.insertion_sort(template2)
    # print srt.insertion_sort(template2, 2)
    # print srt.merge_sort(template1, 7)
    # print srt.merge_sort(template2, 2)
    # print srt.Python_QS(template1)
    # print srt.Python_QS(template2)
    # print srt.heap_sort(template1, len(template1))
    # print srt.heap_sort(template2, len(template2))

    another = Priority_Queue(template1)
    print another.store

    print srt.get_contents()
    print srt
