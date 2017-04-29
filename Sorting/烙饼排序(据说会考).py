import sys

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        return self.pancakeSort(A, len(A))

    def pancakeSort(self, array, length):
        for i in xrange(length - 1, 0, -1):
            cur_max_pos = self.findMax(array, i)
            print cur_max_pos
            if cur_max_pos != i:
                self.reverse(array, cur_max_pos)
                self.reverse(array, i)
                print 'here'
            print array
        return array

    def findMax(self, array, pos):
        q = -sys.maxint
        result = None
        for i in xrange(pos + 1):
            if array[i] > q:
                q = array[i]
                result = i
        return result
    
    def reverse(self, array, pos):
        st, ed = 0, pos
        while st < ed:
            array[st], array[ed] = array[ed], array[st]
            st += 1
            ed -= 1

a = Solution()
print a.sortIntegers([5,3,4,2])
    