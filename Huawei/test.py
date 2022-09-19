# 有一个长长的吊桥，吊桥的尽头是下水管道，其中随机的木板存在缺失，一旦踩到就会死
# 亡，死亡后如果还有剩余的生命将在原地# 复活且不受木板缺失影响，但会消耗一次生命；
# 如果跨过了管道，将跌入悬尾，通关失败。超级玛丽从超点公开始，可以走到下一个木板 
# (计1)，也可以跳着跨过一个块（计2） 或两个木板（计3），最終必须刚好走到终点巨。
# 现在给定超级玛丽当前的生命数M，吊桥的长度N，缺失的木板数K，以及随机缺失的木板
# 编号数组L，请帮忙计-算一下，超级玛丽有多少种方法可以通过此关。

# 输入描述:
# 第一行输入三个整数M，N，K，分别表示超级玛丽的生命数，吊桥的长度，以及随机缺失的
# 木板数，第二行输入K个整数，表示随机缺失的木板编号，木板编号从1开始，到N结束。

# 输出描述:
# 输出一个整数，表示超级玛丽有多少种方法可以通过此关。

# 输入例子1:
# 2 2 1
# 2 4
# 输出例子1:
# 4

from functools import lru_cache
M, N, K = map(int, input().strip().split ())
L = set (map(int, input ().strip().split ()))
@lru_cache(None)

def func(life, idx):
    if life <= 0:
        return 0 
    if idx in L:
        life -= 1 
        if life <= 0:
            return 0
    if idx == 0:
        return 1
    if idx == 1:
        return 1 
    if idx == 2:
        return func(life, idx - 2) + func(life, idx - 1)
    return func(life, idx - 3) + func(life, idx - 2) + func(life, idx - 1)

print (func(M, N + 1))

