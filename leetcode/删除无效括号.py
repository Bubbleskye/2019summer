def removeInvalidParentheses(s):
    from collections import deque
    res = set()
    # 多余左括号的个数
    rmL = 0
    # 多余右括号的个数
    rmR = 0
    for a in s:
        if a == "(":
            rmL = rmL + 1
        elif a == ")":
            if rmL != 0:
                rmL = rmL - 1
            else:
                rmR = rmR + 1

    # 是否满足有效括号
    def isValid(s):
        cnt = 0
        for a in s:
            if a == "(":
                cnt += 1
            elif a == ")":
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

    # 记录此时 s , 左右括号的个数
    queue = deque([(s, rmL, rmR)])
    visited = set()
    visited.add((s, rmL, rmR))
    # bfs
    while queue:
        tmp_s, left_p, right_p = queue.pop()
        # 输出条件
        if left_p == 0 and right_p == 0 and isValid(tmp_s):
            res.add(tmp_s)
        for i in range(len(tmp_s)):
            # 为字母时候
            if tmp_s[i] not in "()":
                continue
            if tmp_s[i] == "(" and left_p > 0:
                # 删除这个括号
                t = tmp_s[:i] + tmp_s[i + 1:]
                if (t, left_p - 1, right_p) not in visited:
                    queue.appendleft((t, left_p - 1, right_p))
                    visited.add((t, left_p - 1, right_p))
            if tmp_s[i] == ")" and right_p > 0:
                # 删除这个括号
                t = tmp_s[:i] + tmp_s[i + 1:]
                if (t, left_p, right_p - 1) not in visited:
                    queue.appendleft((t, left_p, right_p - 1))
                    visited.add((t, left_p, right_p - 1))
    return list(res)

s="()())()"
print(removeInvalidParentheses(s))