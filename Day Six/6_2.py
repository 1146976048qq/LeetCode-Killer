
# 29. 两数相除  
# ***************************************
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# ***************************************
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10 除以 3 得 3 余 1，商为 3 。
# ***************************************
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7 除以 -3 得 -2 余 2，商为 -2 。
# ***************************************
# 输入: dividend = -10, divisor = 3
# 输出: -3
# 解释: -10 除以 3 得 -3 余 -1，商为 -3 。
# ***************************************
# 输入: dividend = -2147483648, divisor = -1
# 输出: 2147483647
# 解释: 2147483648 除以 -1 得 -2147483648 余 0，商为 2147483647 。
# ***************************************
# https://leetcode.cn/problems/divide-two-integers/

class Solution():
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend > 0 and divisor > 0:
            return self.divide_positive(dividend, divisor)
        if dividend < 0 and divisor > 0:
            return -self.divide_positive(-dividend, divisor)
        if dividend > 0 and divisor < 0:
            return -self.divide_positive(dividend, -divisor)
        if dividend < 0 and divisor < 0:
            return self.divide_positive(-dividend, -divisor)
    def divide_positive(self, dividend, divisor):
        ans = 0
        while dividend >= divisor:
            dividend -= divisor
            ans += 1
        return ans


print(Solution().divide(10, 3))
print(Solution().divide(7, -3))
print(Solution().divide(-10, 3))
print(Solution().divide(-2147483648, -1))
# ***************************************
