# 机器人会无限循环地按照 command 中的指令进行移动，我们可以记录下机器人在一次循环中所经过的坐标，后续循环中到达的坐标都可以推测出来。
# 例如，command = 'RRU'，则在一次循环中机器人会经过 (0,0),(1,0),(2,0),(2,1) 这四个点。
# 在第二次循环中它会经过 (3,1),(4,1),(4,2) 这三个点。
# 在第三次循环中他会经过 (5,2),(6,2),(6,3) 这三个点……
# 已知机器人在第一次循环中走过的所有点，和向右移动的总距离 xi，和向上移动的总距离 y。给出任意一个点 (m,n)(m,n)，如何判断这个点是否在机器人的运动轨迹中？
# 我们可以计算出从原点到 (m,n) 需要走多少个循环，也就是横坐标循环的次数与纵坐标循环的次数的较小值：circle = min(m/xi,n/yi)。
# 然后我们就可以得到点 (m,n) 相当于第一次循环中的哪个点。如果这个点在第一次循环的轨迹中，那么机器人一定可以到达这个点。反之则不能到达。
# 然后再去判断障碍点是否在循环中，如果在，则为False

def robot(command, obstacles, x, y):
    xmove = 0
    ymove = 0
    for c in command:
        if c == "U":
            ymove = ymove + 1
        if c == "R":
            xmove = xmove + 1
    lun = min(x // xmove, y // ymove)
    now = [xmove * lun, ymove * lun]
    # 到达这个now之后，判断在一轮之内能否达到目标点
    flag = 0
    if now != [x, y]:
        for c in command:
            if c == "U":
                now[1] = now[1] + 1
            if c == "R":
                now[0] = now[0] + 1
            if now == [x, y]:
                flag = 1
                break
        if flag == 0:
            return False
    for o in obstacles:
        if o[0] > x or o[1] > y:
            continue
        f = 0
        lun = min(o[0] // xmove, o[1] // ymove)
        now = [xmove * lun, ymove * lun]
        if now == o:
            return False
        else:
            for c in command:
                if c == "U":
                    now[1] = now[1] + 1
                if c == "R":
                    now[0] = now[0] + 1
                if now == o:
                    f = 1
                    break
            if f == 1:
                return False
    return True