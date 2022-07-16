
# N个数组的笛卡尔积
# 给定两个数组，写一个函数来计算它们的笛卡尔积
# 输入: [1,2,3] [4,5,6]
# 输出: [1,4,2,5,3,6]
# 解释: [1,4,2] 和 [5,3,6] 的笛卡尔积是 [1,4,2,5,3,6]。
#  ***************************************
# https://leetcode.cn/problems/cartesian-product-of-two-arrays/
# 
# 
class Solution():
    def cartesianProduct(self, A, B):
        res = []
        for a in A:
            for b in B:
                res.append([a,b])
        return res
    
    def cartesianProduct2(self, A, B):
        return [[a,b] for a in A for b in B]


print(Solution.cartesianProduct(Solution, [1,2,3], [4,5,6]))
