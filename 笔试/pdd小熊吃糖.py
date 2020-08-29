def eatSugar(n, m, sugar, bear):
    sugar = sorted(sugar, reverse=True)
    for item in sorted(bear.items(), key=lambda x: x[1], reverse=True):  # 按照字典value排序
        for i in range(m):
            if item[1][1] >= sugar[i]:
                item[1][1] -= sugar[i]
                sugar[i] = 0
    for i in range(n):  # 最终输出结果要求按最早熊的顺序
        print(bear[i][1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    sugar = list(map(int, input().split()))
    # split函数默认以空格和“\n”为分隔符
    # 如果特别限制为" "或"\n"另一种则无用
    bear = {}
    for i in range(n):
        k, v = map(int, input().split())
        bear[i] = [k, v]
    eatSugar(n, m, sugar, bear)
