points=[[0,0],[94911151,94911150],[94911152,94911151]]
if not points:
    print(0)
res = 0
points_dict={}
# 所有点统计
for point in points:
    if tuple(point) not in points_dict:
        points_dict[tuple(point)]=1
    else:
        points_dict[tuple(point)] = points_dict[tuple(point)] + 1
# 把唯一点列举出来
points = list(points_dict.keys())

for i in range(len(points)):
    p0 = points[i]
    j = i + 1
    count = points_dict[p0]
    while j < len(points):
        count = points_dict[p0]
        p1 = points[j]
        if p1[0] != p0[0]:
            tan = (p1[1] - p0[1]) / (p1[0] - p0[0])
        else:
            tan = float('inf')
        count = count + points_dict[p1]
        k = j + 1
        while k < len(points):
            p2 = points[k]
            if p2[0] != p0[0]:
                tmptan1 = (p2[1] - p0[1]) / (p2[0] - p0[0])
            else:
                tmptan1 = float('inf')
            if p2[0] != p1[0]:
                tmptan2 = (p2[1] - p1[1]) / (p2[0] - p1[0])
            else:
                tmptan2 = float('inf')
            if tmptan1 == tan and tmptan2 == tan:
                count = count + points_dict[p2]
            k = k + 1
        res = max(res, count)
        j = j + 1
    res = max(res, count)

print(res)