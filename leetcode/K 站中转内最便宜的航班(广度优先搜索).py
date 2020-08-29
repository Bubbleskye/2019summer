def findCheapestPrice(n, flights, src, dst, K) :
    # 利用字典的广度优先搜索
    from collections import defaultdict, deque
    flight_dict = defaultdict(list)
    for i in range(len(flights)):
        flight_dict[flights[i][0]].append((flights[i][1], flights[i][2]))
        # 字典key：起始点 value:（终止点，价格）
    if src not in flight_dict:
        return -1

    queue = deque()
    # 起点,中转次数,价格
    queue.appendleft((src, 0, 0))
    min_price = float('inf')

    while queue:
        for _ in range(len(queue)):
            #用于得到一层的元素数目
            start, counter, cur_price = queue.pop()
            for end, price in flight_dict[start]:
                # 到达目的地
                if end == dst and counter <= K:
                    min_price = min(min_price, (cur_price + price))
                # 未到目的地,中转次数还未达到上限,目前的价格小于小于最小价格
                # 如果大于最小价格而且还没到目的地,就没有再看的必要了
                # 如果中转次数已达上线,也没有看的必要了
                elif counter <= K and (cur_price + price) < min_price:
                    queue.appendleft((end, counter + 1, cur_price + price))
    if min_price != float('inf'):
        return min_price
    else:
        return -1