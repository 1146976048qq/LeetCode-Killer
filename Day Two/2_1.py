
# 3. 无重复字符的最长子串
# ***************************************
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 你可以认为每个字符串中只有字母（'a'-'z'）和数字（'0'-'9'）。
# ***************************************
# 示例 1：
# 输入: "abcabcbb"
# 输出: 3 

# 示例 2：
# 输入: "bbbbb"
# 输出: 1


# 示例 3：
# 输入: "pwwkew"
# 输出: 3
# 解释: 所有可能的子串都是最长的，只有 "pwke" 是唯一的。
# ***************************************
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution():
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len = 0
        start = 0
        end = 0
        hashtabel = dict()
        while end < len(s):
            if s[end] in hashtabel:
                start = max(start, hashtabel[s[end]] + 1)
            hashtabel[s[end]] = end
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len

print(Solution.lengthOfLongestSubstring("abcabcbb"))
print(Solution.lengthOfLongestSubstring("bbbbb"))
print(Solution.lengthOfLongestSubstring("pwwkew"))
print("***************************************")




