# 一日，师徒四人途径一个m * n 长方形区域，已知：
# 1. 将取经队伍作为一个整体，4人行走相同路线
# 2. 取经队伍的起点为该长方形区域的左上角，目的地为该长方形区域的右下角。
# 3. 行走路线可以向前、后、左、右四个方向前进（不允许超出该长方形区域）
# 4. 输入包含该区域的长m和完n，前后移动允许的高度差t，以及该长方形区域内各点的高度h。
# 5. 要求该区域内相邻两次移动的高度差在高度范国以内。取经队伍最多有3次爆发机会，每使用一次爆发机会，可以让取经队伍一次移动突破高度差垠制

# 请问取经队伍通过该区域最小的移动次数是多少？返回-1表示师徒四人无法直接通过该区域。

# 输入描述:
# 输入包含一个整数m，表示长方形区域的长，再输入一个整数n，表示长方形区域的宽，再输入一个整数t，表示高度差，再输入m * n个整数，表示长方形区域内各点的高度。
# 输出描述:
# 输出一个整数，表示取经队伍通过该区域最小的移动次数，返回-1表示师徒四人无法直接通过该区域。
# 示例1
# 输入
# 4 4 2
# 1 2 3 4
# 输出
# -1
# 样例解释:

# 师徒四人可以直接通过该区域，因为高度差在高度范围内。


def get_min_step(m, n, t, h):
    step = 0
    for i in range(m): # 列 
        for j in range(n):  # 行
            if h[i][j] > h[i][j + 1] + t or h[i][j] > h[i + 1][j] + t:  
                return -1  
            if h[i][j] > h[i][j - 1] + t or h[i][j] > h[i + 1][j] + t:  
                return -1
            if h[i][j] > h[i - 1][j] + t or h[i][j] > h[i][j + 1] + t:
                return -1
            if h[i][j] > h[i - 1][j - 1] + t or h[i][j] > h[i + 1][j + 1] + t:
                return -1
            if h[i][j] > h[i - 1][j + 1] + t or h[i][j] > h[i + 1][j - 1] + t:
                return -1
    return step


if __name__ == '__main__':
    m, n, t = map(int, input().split())
    h = []
    for i in range(m):
        h.append(list(map(int, input().split())))

# print(get_min_step(4, 4, 1, [[1, 2, 3, 4]]))
    # print(get_min_step(4, 4, 2, [[1, 2, 3, 4]]))


    


    

