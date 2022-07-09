
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
