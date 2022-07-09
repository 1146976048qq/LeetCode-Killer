
# 11. 盛最多水的容器
# ***************************************
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# ***************************************
# 示例:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# ***************************************
# https://leetcode.cn/problems/container-with-most-water/


class Solution():
    def MaxArea(height):
        if not height:
            return 0
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, (j - i) * min(height[i], height[j]))
        return max_area

    def MaxArea2(height):
        if not height:
            return 0
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution.MaxArea([1,8,6,2,5,4,8,3,7]))
print(Solution.MaxArea2([1,8,6,2,5,4,8,3,7]))


