
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


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
    
print(Solution.permute(Solution, [1,2,3]))
print(Solution.permute(Solution, [1,2,3,4]))