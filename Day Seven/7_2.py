
# 43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# ***************************************
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# ***************************************
# https://leetcode.cn/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])
        for i in range(0, len(ans)):
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        while ans[-1] == 0:
            ans.pop()
        return ''.join(map(str, ans[::-1]))


print(Solution().multiply('2', '3'))
print(Solution().multiply('123', '456'))
print("***************************************")

