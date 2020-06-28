'''
You are a product manager and currently leading a team to develop a new product.
 Unfortunately, the latest version of your product fails the quality check.
 Since each version is developed based on the previous version, all the
 versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.
'''


'''
The isBadVersion API is already defined for you.
@param version, an integer
@return a bool
def isBadVersion(version):

用的recursive方法进行BS，用迭代速度会变快，居然特么想了半年...
'''

class Solution(object):
    def FBV(self, st, ed):
        if st == ed: return st
        mid = st + (ed - st) / 2
        if isBadVersion(mid): return self.FBV(st, mid)
        else: return self.FBV(mid + 1, ed)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.FBV(1, n)


'''
做lintcode想出来的第二版，既然要求少用API那就多加一个dict记录已经用过的版本
确保以后不再用就行了，无非用空间换时间而已
Beat 89.10%
'''

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        st, ed = 1, n
        tmp = {}
        while st < ed:
            mid = st + (ed - st) / 2
            if tmp.has_key(mid - 1):
                if tmp[mid - 1] == 1:
                    ed = mid
                else:
                    st = mid + 1
            elif isBadVersion(mid):
                ed = mid
                tmp[mid - 1] = 1
            else:
                st = mid + 1
                tmp[mid - 1] = 2
        return st
