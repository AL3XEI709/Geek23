def ant_probability(n, x):
    # 初始化一个二维数组来存储概率分布
    # dp[i][j]表示在i秒内蚂蚁到达坐标j的概率
    dp = [[0.0] * (2 * n + 1) for _ in range(n + 1)]

    # 初始条件：在0秒内，蚂蚁在原点的概率为1
    dp[0][n] = 1.0

    # 开始动态规划计算概率分布
    for t in range(1, n + 1):
        for position in range(2 * n + 1):
            # 蚂蚁在t秒内向正方向前进一个单位
            forward_prob = dp[t - 1][position - 1] * 0.5
            # 蚂蚁在t秒内向负方向前进一个单位
            backward_prob = dp[t - 1][position + 1] * 0.5
            # 更新位置position处的概率
            dp[t][position] = forward_prob + backward_prob

    # 返回n秒后蚂蚁到达x坐标处的概率
    return dp[n][x + n]

# 输入秒数n和目标坐标x
n = int(input("请输入秒数n: "))
x = int(input("请输入目标坐标x: "))

# 计算概率并输出结果
probability = ant_probability(n, x)
print(f"蚂蚁在{n}秒内到达坐标{x}的概率为: {probability}")
