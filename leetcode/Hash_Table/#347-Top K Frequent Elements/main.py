# coding=utf-8

'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
'''

'''
现在这个才是符合要求的做法，显然这道题O(nlgn)是不符合要求的，利用堆和哈希表对
词频进行统计是一个合理的方法，时间复杂度O(nlgk)，这里的方法是利用桶排序，实质
上也就是计数排序对前k个词频进行统计，这样时间复杂度可以达到O(n + k)
公司：Pocket Gems， Yelp
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        freqMap = {}
        bucket = [set([]) for _ in xrange(n + 1)]

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for num in nums:
            bucket[freqMap[num]].add(num)
        
        res = []
        for i in xrange(n , -1, -1):
            if bucket[i]:
                for ent in bucket[i]:
                    if k == 0:
                        break
                    res.append(ent)
                    k -= 1
            if k == 0:
                return res
        
        return res

        
