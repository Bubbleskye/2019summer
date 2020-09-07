# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)
# 为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
#
# 示例 1:
#
# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 示例 2:
#
# 输入: [[7,10],[2,4]]
# 输出: 1

def minMeetingRooms(intervals):
# 按照 开始时间 对会议进行排序。
# 初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
# 对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
# 若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
# 若房间不空闲。开新房间，并加入到堆中。
# 处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。
    import heapq
    intervals.sort(key= lambda x: x[0])
    row=len(intervals)
    if row==0:
        return 0
    free_room=[]
    heapq.heappush(free_room,intervals[0][1])
    for i in range(1,row):
        if intervals[i][0]<free_room[0]:
            # 用开始时间跟结束时间比较，确定是否能用之前的房间
            # 如果开始时间小于最小的结束时间，则另开一个房间
            heapq.heappush(free_room,intervals[i][1])
        else:
            heapq.heappushpop(free_room,intervals[i][1])
    return len(free_room)