
# 44. 数组中的第K个最大元素
# ***************************************
# 给定一个数组，请你在该数组中找出第 k 个最大的元素。
# 请你实现这个函数，返回第 k 个最大的元素。
# 请你在O(n)时间复杂度和O(1)空间复杂度内完成此操作。
# ***************************************
# 示例 1:
# 输入: nums = [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
# 输入: nums = [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
# 示例 3:
# 输入: nums = [1], k = 1
# 输出: 1
# ***************************************
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
#

class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(Solution().findKthLargest([1], 1))
print("***************************************")
