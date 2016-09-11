# coding=utf-8

from SortingAL import *

if __name__ == '__main__':
    template1 = [3, 4, 9, -10, 20, 0, 156]
    template2 = [1, 0]
    template3 = [34,3,4,6,7,1,6,7,8,3,4,23,6]
    srt = Mode()
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
    print srt.counting_sort(template3)
