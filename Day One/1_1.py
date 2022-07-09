
# 873. 最长的斐波那契子序列的长度
# ***************************************
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
# （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。
# 例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
# ***************************************
# 示例 1：
# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

# 示例 2：
# 输入: arr = [1,3,7,11,12,14,18]
# 输出: 3
# 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
# ***************************************
# 解题思路：
# 1. 暴力解法：
#   a. 初始化：
#     1. 初始化一个数组，用来存储每个数字的斐波那契式子序列的长度，初始化为0，即当前数字自身。
#   b. 循环：
#     1. 循环遍历数组，每次循环，都会计算当前数字的斐波那契式子序列的长度。
#     2. 如果当前数字的斐波那契式子序列的长度大于最大值，则更新最大值。
#   c. 返回最大值。
# 2. 动态规划：
#   a. 初始化：
#     1. 初始化一个数组，用来存储每个数字的斐波那契式子序列的长度，初始化为0，即当前数字自身。

# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/


class Solution:
    def lenLongestFibSubseq(arr):
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr):
            for j in range(n - 1, -1, -1):
                if arr[j] * 2 <= x:
                    break
                if x - arr[j] in indices:
                    k = indices[x - arr[j]]
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans

    def lenLongestFibSubseq2(A):
        dp = {}
        for i, x in enumerate(A):
            dp[x] = i
        ans = 0
        for i, x in enumerate(A):
            for j in range(i + 1, len(A)):
                y = x + A[j]
                if y in dp:
                    ans = max(ans, dp[y] - i + 1)
        return ans

print(Solution.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(Solution.lenLongestFibSubseq([1,3,7,11,12,14,18]))
print("***************************************")
print(Solution.lenLongestFibSubseq2([1,2,3,4,5,6,7,8]))
print(Solution.lenLongestFibSubseq2([1,3,7,11,12,14,18]))

