
# 字节跳动面试题
#  ***************************************
# 输入是二维数组，打印其笛卡尔积
# 输入：[[1,2,3],[5,6],[7,8]]
# 输出：[[1,5,7],[1,5,8],[1,6,7],[1,6,8],[2,5,7],[2,5,8],[2,6,7],[2,6,8],[3,5,7],[3,5,8],[3,6,7],[3,6,8]]
#  ***************************************
# https://leetcode.cn/problems/cartesian-product-of-two-arrays/
#
#
def Solution(arrays):
    res = []
    def multiCar(arr, i, r):
        # i index
        # r result

        if i == len(arr):
            res.append(r) 
        else:
            for j in range(len(arr[i])):
                multiCar(arr, i + 1, r + str([arr[i][j]]))   # 将当前元素加入结果中
    
    multiCar([[1,2,3],[5,6],[7,8]], 0, '') # 开始递归
    return res

print(Solution([[1,2,3],[5,6],[7,8]]))