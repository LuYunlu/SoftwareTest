

def distance(w1, w2):
    d = abs(w2 - w1)
    return d


def calsimilarity(selectvalues):
    # 1~20.csv里的数据分别与0.csv中的比较
    p = selectvalues[0]
    m = len(p)
    simi = {}
    for k in range(1, 21):
        y = selectvalues[k]
        n = len(y)

        # 构建二位dp矩阵,存储对应每个子问题的最小距离
        dp = [[0] * n for _ in range(m)]

        # 起始条件,计算单个字符与一个序列的距离
        for i in range(m):
            dp[i][0] = distance(p[i], y[0])
        for j in range(n):
            dp[0][j] = distance(p[0], y[j])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + distance(p[i], y[j])

        parm = dp[-1][-1]
        simi[parm] = k
    simi = sorted(simi.items())
    nameofrank1 = simi[0][1]  # rank1 = selectvalues[nameofrank1]
    nameofrank2 = simi[1][1]  # rank2 = selectvalues[nameofrank2]
    nameofrank3 = simi[2][1]  # rank3 = selectvalues[nameofrank3]
    return nameofrank1, nameofrank2, nameofrank3

    # p = selectvalues[0]
    # x = []
    # simi = []
    # for i in range(61):
    #     x.append(i)  # print(len(x))
    # for k in range(1, 21):
    #     y = selectvalues[k]
    #     distances = np.zeros((61, 61))
    #     for i in range(61):
    #         for j in range(61):
    #             distances[i, j] = (p[j] - y[i]) ** 2
    #     accumulated_cost = np.zeros((61, 61))
    #     accumulated_cost[0, 0] = distances[0, 0]
    #     for i in range(1, len(p)):
    #         accumulated_cost[0, i] = distances[0, i] + accumulated_cost[0, i - 1]
    #     for i in range(1, len(y)):
    #         accumulated_cost[i, 0] = distances[i, 0] + accumulated_cost[i - 1, 0]
    #     for i in range(1, len(y)):
    #         for j in range(1, len(p)):
    #             accumulated_cost[i, j] = min(accumulated_cost[i - 1, j - 1], accumulated_cost[i - 1, j],
    #                                          accumulated_cost[i, j - 1]) + distances[i, j]
    #     parm = accumulated_cost[60, 60]
    # path = [[len(p) - 1, len(y) - 1]]
    # i = len(y) - 1
    # j = len(p) - 1
    # while i > 0 and j > 0:
    #     if i == 0:
    #         j = j - 1
    #     elif j == 0:
    #         i = i - 1
    #     else:
    #         if accumulated_cost[i - 1, j] == min(accumulated_cost[i - 1, j - 1], accumulated_cost[i - 1, j],
    #                                              accumulated_cost[i, j - 1]):
    #             i = i - 1  # 来自于左边
    #         elif accumulated_cost[i, j - 1] == min(accumulated_cost[i - 1, j - 1], accumulated_cost[i - 1, j],
    #                                                accumulated_cost[i, j - 1]):
    #             j = j - 1  # 来自于下边
    #         else:
    #             i = i - 1  # 来自于左下边
    #             j = j - 1
    #     path.append([j, i])
    # path.append([0, 0])
    # path_px = [point[0] for point in path]
    # path_yx = [point[1] for point in path]
    # parm = 0
    # for i in range(len(path)):
    #     parm = parm + ((path_px[i] - path_yx[i]) ** 2 + (p[path_px[i]] - y[path_yx[i]]) ** 2)
