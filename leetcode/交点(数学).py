def intersection(start1, end1, start2, end2):
    # 首先假设一点，end一定在start的上方（y值），如果初始传入的不满足，则进行交换
    if end1[1] < start1[1]:
        start1, end1 = end1, start1
    if end2[1] < start2[1]:
        start2, end2 = end2, start2

    # 一般表达式，y=kx+b，如果是垂直于x轴的，我们把k设为None，b设为x就好。
    if start1[0] != end1[0]:
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0])
        b1 = start1[1] - k1 * start1[0]
    else:
        k1 = None
        b1 = None
    if start2[0] != end2[0]:
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0])
        b2 = start2[1] - k2 * start2[0]
    else:
        k2 = None
        b2 = None

    if k1 == k2:
    # 平行
        if k1 == None:
        # 两条线都垂直
            if start1[0] == start2[0]:  # 共线
                if start2[1] > end1[1] or start1[1] > end2[1]:
                    # 无相交部分
                    return {}
                elif start1[1] <= start2[1] <= end1[1]:
                    # 有交点，x相同返回y值最小的值
                    return start2
                elif start2[1] <= start1[1] <= end2[1]:
                    return start1
            else:  # 不共线
                return {}
        elif b1 == b2:
        # 共线
            if k1 >= 0:  # 直线为递增趋势
                if start2[1] > end1[1] or start1[1] > end2[1] :
                    # 无相交部分
                    return {}
                elif start1[1] <= start2[1] <= end1[1]:
                    return start2
                elif start2[1] <= start1[1] <= end2[1]:
                    return start1
            elif k1 < 0:  # 直线为递减趋势
                if start1[1] > end2[1] or start2[1] > end1[1]:
                    return {}
                elif start1[1] <= end2[1] <= end1[1]:
                    return end2
                elif start2[1] <= end1[1] <= end2[1]:
                    return end1
        else:
        # 平行但不共线，所以没有交点
            return {}
    else:
        # 不平行/相交
        if k1 == None:  # 第一条直线垂直，第二条不垂直
            if start1[0] < start2[0] or end2[0] < start1[0]:
                return {}
            else:
                if start1[1] <= k2 * start1[0] + b2 <= end1[1]:
                    return [start1[0], k2 * start1[0] + b2]
                else:
                    return {}
        elif k2 == None:  # 第二条直线垂直，第一条不垂直
            if start2[0] < start1[0] or end1[0] < start2[0]:
                return {}
            else:
                if start2[1] <= k1 * start2[0] + b1 <= end2[1]:
                    return [start2[0], k1 * start2[0] + b1]
                else:
                    return {}
        else:  # 最一般的情况，直接计算两条直线交点，判断交点和线段的位置关系即可
            t_x = (b2 - b1) / (k1 - k2)
            t_y = k1 * t_x + b1
            if min(start1[0], end1[0]) <= t_x <= max(start1[0], end1[0]) and min(start2[0], end2[0]) <= t_x <= max(
                    start2[0], end2[0]):
                # 如果交点的x值在两条线start的x值与end的x值之间
                return [t_x, t_y]
            else:
                return {}
