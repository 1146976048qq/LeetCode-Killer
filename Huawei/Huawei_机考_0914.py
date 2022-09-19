#### code 1 ###### #### code 1 ######
#### code 1 ###### #### code 1 ######
#### code 1 ###### #### code 1 ######

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








##### code 2 #####   ##### code 2 #####
##### code 2 #####   ##### code 2 #####
##### code 2 #####   ##### code 2 #####

# 有一批数据包需要传输，每个数据包大小不一样，传输需要不同的时长，现在有N个传输通道，
# 每个通道的大小也不一样，通道只能传输小于等于自己大小的数据包，不同通道可以同时传输
# 数据包，通道中可以缓存多个数据包，当新任务来时，可以先进入缓存队列等待发送，问最短
# 需要多长时间能够传输完成，通道会确保所有数据包都可以传输。
# 输入描述:
# 第一行输入两个整数N和M，N表示通道数量，M表示数据包数量
# 第二行输入N个整数，表示每个通道的大小P
# 第三行输入M个整数，表示每个数据包的大小Q
# 第四行输入M个整数，表示每个数据包的传输时长S
# 输出描述:
# 输出一个整数，表示最短传输时长
# 输入例子1:
# 5 2
# 5 3
# 1 4 5 2 3
# 1 6 10 3 4
# 输出例子1:
# 16
# 例子说明1:
# 数据包3进入通道1，数据包2进入通道1，数据包5进入通道2，数据包4进入通道2，数据包1进入通道2；
# 通道1的传输时长是10+6=16，通道2的传输时长是3+2+1=8，这样最短时长就为16
# 
# 有一批数据包需要传输，每个数据包大小不一样，传输需要不同的时长，现在有N个传输通道，
# 每个通道的大小也不一样，通道只能传输小于等于自己大小的数据包，不同通道可以同时传输
# 数据包，通道中可以缓存多个数据包，当新任务来时，可以先进入缓存队列等待发送，问最短
# 需要多长时间能够传输完成，通道会确保所有数据包都可以传输。
# 输入描述:
# 第一行输入两个整数N和M，N

def main():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    S = list(map(int, input().split()))
    # print(N, M, P, Q, S)
    # 通道
    channel = [0] * N
    # 缓存
    cache = []
    # 传输时长
    time = 0
    # 数据包
    for i in range(M):
        # 通道
        for j in range(N):
            # 通道空闲
            if channel[j] == 0:
                # 数据包大小小于等于通道大小
                if Q[i] <= P[j]:
                    # 将数据包传输到通道
                    channel[j] = S[i]
                    break
            # 通道非空闲
            else:
                # 数据包大小小于等于通道大小
                if Q[i] <= P[j]:
                    # 将数据包加入缓存
                    cache.append((j, S[i]))
                    break
        # 通道都满了
        else:
            # 将数据包加入缓存
            cache.append((-1, S[i]))
    # print(channel, cache)
    # 传输时长
    while True:
        # 通道
        for j in range(N):
            # 通道非空闲
            if channel[j] > 0:
                # 通道传输时长减一
                channel[j] -= 1
        # 通道
        for j in range(N):
            # 通道空闲
            if channel[j] == 0:
                # 缓存非空
                if cache:
                    # 从缓存中取出数据包
                    (j, s) = cache.pop(0)
                    # 将数据包传输到通道
                    channel[j] = s
        # 通道
        for j in range(N):
            # 通道非空闲
            if channel[j] > 0:
                # 传输时长加一
                time += 1
                break
        # 通道
        else:
            # 传输时长加一
            time += 1
            break
    # 输出传输时长
    print(time)
    
if __name__ == '__main__': 
    main()




##### code 3 ##### ##### code 3 #####
##### code 3 ##### ##### code 3 #####
##### code 3 ##### ##### code 3 #####
# H公司新接了一个订单，需要帮助容户给一个1P传输网络 （该网络由M个路由器组成，
# 每个路由器与其它多个路由器之问物理连接固定）规划路由，使尸报文从起点到終点，
# 传输距高最小。IP报文在传输时，有如下限制：
# 1. 1P报文头部有丁TL字段代表生存周期。报文从起点经过中间多个路由器转发到终点，
# 每经过一个路由器，生存周期减一。当生存周期为0时，报文被丢弃。
# 2. 超点的1P报文的TTL为固定值，由输入参数给出。

# 输入描述：
# 第一行：4个正整数，分别表示路由器连接边个数N，起点路由器D，終点路由器ID，起点
# 路由器的TTL值。
# 第二行~ 第N+1行，每行3个正整数，分别表示路由器之间的连接关系，以及连接距离。
# 输出描述：
# 1行，2个正整数，分别表示最短距离和剩余TTL值。


from collections import defaultdict
n, s_id, e_id, ttl = map(int, input().strip().split())
edges = defaultdict (list)
max_idx = 0
for _ in range(n):
    s, e, dist = map(int, input().strip() .split ())
    edges [s].append ( [e, dist]) 
    edges [e].append([s, dist])

visit = set()
min_dist = float ('inf')
left_ttl= 0

def dfs(idx, ttl, dist):
    global min_dist, left_ttl
    if (idx != e_id and ttl <= 0) or idx in visit:
        return
    if idx == e_id:
        if min_dist > dist or (min_dist == dist and ttl > left_ttl):
            min_dist = dist
            left_tt1 = ttl
        return
    visit.add (idx)
    for edge in edges [idx]:
        dfs(edge[0], ttl - 1, dist + edge[1]) 
    visit.discard(idx)
dfs(s_id, ttl, 0)
if min_dist != float('inf'):
    print(min_dist, left_ttl) 
else:
    print(-1)
