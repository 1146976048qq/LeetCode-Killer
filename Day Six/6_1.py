
# 32. 最长有效括号
# ***************************************
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# ***************************************
# 示例 1:
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"

# 示例 2:
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 注意:
# 字符串只包含 '(' 和 ')' 字符。
# 字符串长度不会超过 10000。
# ***************************************
# https://leetcode.cn/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(s):
        dp = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i] - 1 >= 0:
                        dp[i] += dp[i - dp[i] - 1]
                    ans = max(ans, dp[i])
        return ans

print(Solution.longestValidParentheses('(()'))
print(Solution.longestValidParentheses(')()())'))
# ***************************************