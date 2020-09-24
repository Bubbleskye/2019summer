numCourses=3
prerequisites=[[0,1],[0,2],[2,1]]
# 拓扑排序

# 记录要学习 index 表示的课程前得学习多少其他课程
marks = [0 for _ in range(numCourses)]
# 记录学完 index 表示的课程后可学习的课程的集合
relation = [[] for _ in range(numCourses)]

for cur, pre in prerequisites:
    # 表示学习 cur 课程前得学习 marks[cur] 个课程
    marks[cur] += 1
    # 学习完 pre 课程就可以学习 relation[pre] 集合中的课程了
    relation[pre].append(cur)

from collections import deque
queue = deque()

for course in range(numCourses):
    if marks[course] == 0: # 学习 course 课程不需要先学习其他课程
        queue.append(course)

while queue:
    course = queue.popleft()
    # 学习完了一个课程
    numCourses -= 1
    for next_course in relation[course]:
        # next_course 的前置课程数量减少一个，因为 course 学完了
        marks[next_course] -= 1
        if marks[next_course] == 0: # 表示学习 next_course 不需要先学习其他课程了
            queue.append(next_course)
print(numCourses == 0)
