'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems

'''

# 直接用等号赋值的list是和C++中一样相当于用指针关联起来的，任何的改变在两边都会产生一样效果

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = [s for s in nums]  # 此处必须重新将值遍历到temp里去，不能直接等号赋值
        temp.sort()
        st = 0
        end = len(nums) - 1
        result = []
        while st < end:
            if temp[st] + temp[end] > target: end -= 1
            elif temp[st] + temp[end] < target: st += 1
            else:

# 当两值相等时，需要重新确定第二个点在原list里面的坐标

                if temp[st] == temp[end]:
                    result.append(nums.index(temp[st]))
                    second = nums.index(temp[st])
                    result.append(nums[second + 1: ].index(temp[end]) + second + 1)
                    return result
                else:
                    result.append(nums.index(temp[st]))
                    result.append(nums.index(temp[end]))
                    return result

        return result
