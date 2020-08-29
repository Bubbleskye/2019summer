def canMeasureWater( x, y, z):
    # 深度优先搜索
    stack = [(0, 0)]
    # x/y中的水量
    seen = set()
    # 存储已经有过的状态
    while stack:
        remain_x, remain_y = stack.pop()
        if remain_x == z or remain_y == z or remain_x + remain_y == z:
            return True
        if (remain_x, remain_y) in seen:
            continue
        seen.add((remain_x, remain_y))
        # 把 X 壶灌满。
        stack.append((x, remain_y))
        # 把 Y 壶灌满。
        stack.append((remain_x, y))
        # 把 X 壶倒空。
        stack.append((0, remain_y))
        # 把 Y 壶倒空。
        stack.append((remain_x, 0))
        # 把 X 壶的水灌进 Y 壶，直至灌满y或倒空x。
        stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
        # 把 Y 壶的水灌进 X 壶，直至灌满x或倒空y。
        stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
    return False