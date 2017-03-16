# coding=utf-8

'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result.
Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

'''
用randint包就行了，用一次减一个数规模，Beat 49.02%
'''

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.store = nums[:]
        self.tmp = nums[:]
        self.n = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.store

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = []
        while self.n:
            pick = random.randint(0, self.n - 1)
            self.tmp[pick], self.tmp[-1] = self.tmp[-1], self.tmp[pick]
            res.append(self.tmp.pop())
            self.n -= 1
        self.n = len(self.store)
        self.tmp = self.store[:]
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
