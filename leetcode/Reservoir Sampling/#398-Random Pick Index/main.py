# coding=utf-8

'''
Given an array of integers with possible duplicates, randomly output the
index of a given target number. You can assume that the given target number
must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space
will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly.
Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''

'''
自己的做法也能过，但是是纯随机取样，时间很慢，有时候还会TLE没有价值
下面这个是真正的reservoir sampling做法
Beat 50.60%
公司：Facebook
'''

'''
Do we want to optimize run time or memory?If we want to optimize run time
then we can use a dictionary to pre-process the nums array.
Simply create a map of key (number) and value (list of its indices).
Then run reservoir sampling over this input.
But the problem statement says that using too much memory is not allowed.
In that case, we can iterate the entire array and keep a variable to track
the frequency of the target for input into reservoir sampling.
Notice random() returns uniform random number between [0 to 1]
'''

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 1
        res = None
        for index, num in enumerate(self.nums):
            if num == target:
                if random.randint(1, count) == 1:
                    res = index
                count += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
