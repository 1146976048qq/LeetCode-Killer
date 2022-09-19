# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 示例 1: 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2: 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3: 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 示例 4: 
# 输入: s = ""
# 输出: 0

class Solution:
    def AAA (self, s):
        if not s:
            return 0
        char_map = [-1]*256
        max_sub = 1
        be = 1
        char_map[ord(s[0])] = 0
        for i in range(1, len(s)):
            start = i - char_map[ord(s[i])]
            next = be + 1
            current = min(start, next)
            max_sub = max(max_sub, current)
            be = current
            char_map[ord(s[i])] = i
        return max_sub

print(Solution().AAA('abcabcbb'))
print(Solution().AAA('bbbbb'))
print(Solution().AAA('pwwkew'))
print(Solution().AAA(''))


