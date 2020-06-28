# coding=utf-8

'''
Given an array nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the
sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size
for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements
that need to be considered.
'''

'''
按照牛客网上面的做法实现的，其实思路确实是堆的原理
用qmax保存下标
General的情况下，qmax为空时（这种情况只可能发生在刚开始遍历时），直接append
qmax不为空时，如果qmax[-1]小于等于当前值，则一直pop直到qmax为空或者qmax[-1]
大于当前值为止，然后再append，这么做原因在于如果当前值大，之前的qmax存储的值就没有
保存的意义了，用当前值就可以满足之后K个遍历的最大值了
如果qmax[-1]大于当前值，直接append就行了，因为要防止qmax[0]在当前位置是过期的，
即qmax[0]的下标已经不在当前windows里面了
接下来检查qmax[0]的下标是否已经过期，即st+1-k是不是已经大于qmax[0],大于的话
将qmax[0] popleft出去
最后检查当前位置是否已遍历至少K个数从而append最大值进res里面
最后qmax在python中可以用list直接实现也可以用deque实现
Beat 74.50%
公司:Amazon, Google, Zenefits
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        qmax = collections.deque([])
        st, ed = 0, len(nums) - 1
        res = []
        while st <= ed:
            if not qmax:
                qmax.append(st)
            elif nums[qmax[-1]] <= nums[st]:
                while qmax and nums[qmax[-1]] <= nums[st]:
                    qmax.pop()
                qmax.append(st)
            else:
                qmax.append(st)
            if qmax[0] < (st + 1 - k):
               qmax.popleft()
            if st + 1 >= k:
                res.append(nums[qmax[0]])
            st += 1
        return res
