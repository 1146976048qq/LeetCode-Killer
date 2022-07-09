
# 7. 整数反转
# ***************************************
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# ***************************************
# 示例 1：
# 输入: 123
# 输出: 321
#
# 示例 2：
# 输入: -123
# 输出: -321
#
# 示例 3：
# 输入: 120
# 输出: 21
# ***************************************
# 解题思路：
# 1. 暴力解法：
#   a. 分两步：
#     i. 先将整数转换为字符串
#     ii. 再将字符串转换为整数
#   b. 反转字符串
#   c. 将字符串转换为整数
#   d. 将整数转换为字符串   
# 2. 利用Python的内置函数
#   a. int(str, base)
#   b. str(int, base)
# ***************************************
# https://leetcode.cn/problems/reverse-integer/

class Solution():
    def reverse(x):
        if x == 0:
            return 0
        if x < 0:
            x = -x
            x = int(str(x)[::-1])
            x = -x
        else:
            x = int(str(x)[::-1])
        if x > 2147483647 or x < -2147483648:
            return 0
        return x

print(Solution.reverse(123))
print(Solution.reverse(-123))
print(Solution.reverse(120))
print("***************************************")
