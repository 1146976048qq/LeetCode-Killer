
# 300. 最长上升子序列
# 给定一个无序的整数数组，找到最长上升子序列的长度。
# ***************************************
# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# ***************************************
# https://leetcode.cn/problems/longest-increasing-subsequence/
#

class Solution():
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 示例1
nums1 = [10,9,2,5,3,7,101,18]

print(Solution().lengthOfLIS(nums1))
print("***************************************")

