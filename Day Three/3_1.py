
# 46. 全排列

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# ***************************************   
# 示例:
# 输入: [1,2,3]
# 输出:
# [
#  [1,2,3],
# [1,3,2],
# [1,2,3],
# [2,1,3],
# [2,3,1],
# [3,1,2],
# [3,2,1]
# ]
# ***************************************
# https://leetcode.cn/problems/permutations/

class Solution():
    def permute(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            tmp = nums[i]
            nums.pop(i)
            for j in self.permute(nums):
                result.append([tmp] + j)
            nums.insert(i, tmp)
        return result


print(Solution.permute([1,2,3]))
print(Solution.permute([1,2,3,4]))