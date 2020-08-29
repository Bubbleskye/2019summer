# 这个「嵌套深度」就是输入字符串，使用栈完成括号匹配，栈中最多连续出现的左括号 ( 的个数
# 所以分组，即保证连续的左括号 (( 不被分在同一组，否则会叠加深度

def maxDepthAfterSplit(seq):
    stack = []
    res = []
    for i in range(len(seq)):
        if seq[i] == "(":
            if len(stack) == 0:
                stack.append([seq[i], 0])
                res.append(0)
            else:
                res.append(1 - stack[-1][1])
                stack.append([seq[i], 1 - stack[-1][1]])

        else:
            tmp = stack.pop()
            res.append(tmp[1])
    return res
