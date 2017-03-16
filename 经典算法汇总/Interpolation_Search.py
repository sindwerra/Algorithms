class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if not A:
            return -1
        st, ed = 0, len(A) - 1
        while A[st] != A[ed] and target >= A[st] and target <= A[ed]:
            mid = st + (target - A[st]) * (ed - st) / (A[ed] - A[st])
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                st = mid + 1
            else:
                ed = mid - 1

        if target == A[st]:
            return st
        else:
            return -1
