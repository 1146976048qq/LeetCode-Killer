
# 45. 数组中重复的数字
# ***************************************
# 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# ***************************************
# 示例 1:
# 输入: [2,3,1,0,2,5,3]
# 输出: 2 或 3
# 示例 2:
# 输入: [2,4,3,5,1]
# 输出: 4
# 示例 3:
# 输入: [0,1,2,3,4,5,6,7,8,9]
# 输出: -1
# ***************************************
# https://leetcode.cn/problems/find-the-duplicate-number/
#

class Solution():
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return -1


print(Solution().findDuplicate([2,3,1,0,2,5,3]))
print(Solution().findDuplicate([2,4,3,5,1]))
print(Solution().findDuplicate([0,1,2,3,4,5,6,7,8,9]))
print("***************************************")