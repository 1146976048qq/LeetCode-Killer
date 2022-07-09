
# 1. 两数之和
# ***************************************
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# ***************************************
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# ***************************************
# https://leetcode.cn/problems/two-sum/


class Solution():
    def TwoSum(arr, target):
        len_n = len(arr)
        for i in range(len_n):
            for j in range(i+1, len_n):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return []

print(Solution.TwoSum([2,7,11,15], 9))
print(Solution.TwoSum([3,2,4], 6))
print(Solution.TwoSum([3,3], 6))

print("***************************************")

class Solution2():
    def TwoSum(arr, target):
        hashtabel = dict()
        for i, num in enumerate(arr):
            if target - num in hashtabel:
                return [hashtabel[target - num], i]
            hashtabel[num] = i
        return []
print(Solution2.TwoSum([2,7,11,15], 9))
print(Solution2.TwoSum([3,2,4], 6))
print(Solution2.TwoSum([3,3], 6))
