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
# 4 4 10
# 10 20 30 40
# 100 120 140 160
# 200 220 240 260
# 300 320 340 360
# 输出
# 2

# 思路：
# 1. 初始化取经队伍的起点为左上角，目的地为右下角
# 2. 初始化取经队伍的移动次数为0
# 3. 初始化取经队伍的移动路线为向前移动
# 4. 初始化取经队伍的爆发次数为0
# 5. 初始化取经队伍的爆发路线为向前爆发
# 6. 初始化取经队伍的爆发距离为0

# 7. 如果取经队伍的爆发次数大于等于3，则返回-1
# 8. 如果取经队伍的爆发距离大于等于高度差，则返回-1
# 9. 如果取经队伍的爆发路线为向前爆发，则取经队伍的爆发距离加1
# 10. 如果取经队伍的爆发路线为向后爆发，则取经队伍的爆发距离减1
# 11. 如果取经队伍的爆发路线为向左爆发，则取经队伍的爆发距离加1
# 12. 如果取经队伍的爆发路线为向右爆发，则取经队伍的爆发距离减1
# 13. 如果取经队伍的爆发路线为向上爆发，则取经队伍的爆发距离加1
# 14. 如果取经队伍的爆发路线为向下爆发，则取经队伍的爆发距离减1
# 15. 如果取经队伍的爆发路线为向左向上爆发，则取经队伍的爆发距离加1
# 16. 如果取经队伍的爆发路线为向右向上爆发，则取经队伍的爆发距离减1
# 17. 如果取经队伍的爆发路线为向左向下爆发，则取经队伍的爆发距离加1
# 18. 如果取经队伍的爆发路线为向右向下爆发，则取经队伍的爆发距离减1


def qq(m, n, t, h):
    # 初始化取经队伍的起点为左上角，目的地为右下角
    qj_x = 0
    qj_y = 0
    qj_z = 0
    # 初始化取经队伍的移动次数为0
    qj_move_count = 0
    # 初始化取经队伍的移动路线为向前移动
    qj_move_way = 'forward'
    # 初始化取经队伍的爆发次数为0
    qj_bomb_count = 0
    # 初始化取经队伍的爆发路线为向前爆发
    qj_bomb_way = 'forward'
    # 初始化取经队伍的爆发距离为0
    qj_bomb_distance = 0
  

class qq:
    def __init__(self, m, n, t, h):
        self.m = m  # 长方形区域的长
        self.n = n  # 长方形区域的宽
        self.t = t  # 高度差
        self.h = h  # 长方形区域的每个点的高度

    def qq(self):   # 判断是否可以直接通过
        # if self.m < 5 or self.n < 5:    # 如果长或宽小于4，则无法直接通过
        #     return -1   # 返回-1
        for i in range(self.m):  # 循环遍历长方形区域的每个点
            for j in range(self.n): # 循环遍历长方形区域的每个点
                if self.h[i][j] > self.h[i][j + 1] + self.t or self.h[i][j] > self.h[i + 1][j] + self.t: # 如果当前点的高度大于下一个点的高度加上高度差，则无法直接通过
                    return -1   # 返回-1
        return self.m * self.n - 1  # 如果所有点都可以直接通过，则返回长方形区域的面积减去1


if __name__ == '__main__':
    m, n, t = map(int, input().split())
    h = []
    for i in range(m):
        h.append(list(map(int, input().split())))
    qq = qq(m, n, t, h)
    print(qq.qq())


class qq:
    def __init__(self, m, n, t, h):
        self.m = m  # 长方形区域的长
        self.n = n  # 长方形区域的宽
        self.t = t  # 高度差
        self.h = h  # 长方形区域的每个点的高度

    def qq(self):   # 判断是否可以直接通过
        # if self.m < 5 or self.n < 5:    # 如果长或宽小于4，则无法直接通过
        #     return -1   # 返回-1
        for i in range(self.m):  # 循环遍历长方形区域的每个点
            for j in range(self.n): # 循环遍历长方形区域的每个点
                if self.h[i][j] > self.h[i][j + 1] + self.t or self.h[i][j] > self.h[i + 1][j] + self.t: # 如果当前点的高度大于下一个点的高度加上高度差，则无法直接通过
                    return -1   # 返回-1
        return self.m * self.n - 1  # 如果所有点都可以直接通过，则返回长方形区域的面积减去1


if __name__ == '__main__':
    m, n, t = map(int, input().split())
    h = []
    for i in range(m):
        h.append(list(map(int, input().split())))
    qq = qq(m, n, t, h)
    print(qq.qq())






