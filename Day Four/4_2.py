
# 26. 删除有序数组中的重复项
# 给定一个有序数组，你需要原地删除其中的重复内容，使得每个元素只出现一次,并返回数组新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# ***************************************
# 示例 1:
# 给定 nums = [1,1,2],
# 函数应该返回新长度为 2 的数组，
# 并且 nums 中的前两个元素必须是 1 和 2。
# 你不需要考虑数组中超出新长度后面的元素。
# ***************************************
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
print(Solution.removeDuplicates(Solution, [1,1,2]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3,4]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3,4,4]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3,4,4,5]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3,4,4,5,5]))
print(Solution.removeDuplicates(Solution, [1,1,2,2,3,3,4,4,5,5,6]))