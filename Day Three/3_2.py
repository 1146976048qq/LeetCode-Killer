
# 8. 字符串转换整数 (atoi)
# ***************************************
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号
# 如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 说明：
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31, 2^31 − 1]。
# 如果数值超过这个范围，请返回 INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
# ***************************************
# 示例 1:
# 输入: "42"
# 输出: 42
#
# 示例 2:
# 输入: "   -42"
# 输出: -42
#
# 示例 3:
# 输入: "4193 with words"
# 输出: 4193
#
# 示例 4:
# 输入: "words and 987"
# 输出: 0
#
# 示例 5:
# 输入: "-91283472332"
# 输出: -2147483648
# ***************************************
# https://leetcode.cn/problems/string-to-integer-atoi/


class Solution():
    def myAtoi(str):
        if not str:
            return 0
        str = str.strip()
        if not str:
            return 0
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]
        else:
            sign = 1
        res = 0
        for i in str:
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
        res = sign * res
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res


print(Solution().myAtoi('42'))
print(Solution().myAtoi('   -42'))
print(Solution().myAtoi('4193 with words'))
print(Solution().myAtoi('words and 987'))
print(Solution().myAtoi('-91283472332'))



