
# 输入是二维数组，打印其笛卡尔积
# 输入：[[1,2,3],[5,6],[7,8]]
# 输出：[[1,5,7],[1,5,8],[1,6,7],[1,6,8],[2,5,7],[2,5,8],[2,6,7],[2,6,8],[3,5,7],[3,5,8],[3,6,7],[3,6,8]]
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


print(Solution.cartesianProduct(Solution, [[1,2,3],[5,6],[7,8]]))