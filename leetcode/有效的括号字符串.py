def checkValidString(s):
    if not s:
        return True
    if s[0] == ")":
        return False
    # 使用两个栈，left存左括号，star存“*”，存储的内容是字符在字符串中的下标。
    # 遍历字符串的每一个字符，如果是“（”存储下标到left中；
    # 如果是“*”存储下标到star中；
    # 如果是“）”，先从left中获取“（”，并将栈顶元素出栈，如果left为空，则从star中获取“*”，将栈顶元素出栈，如果star也为空，则返回false；
    # 按照1 2 3 遍历完字符串之后，遍历left，与“*”匹配；
    # 如果left为空，返回true；
    # 如果left不为空，遍历left，从star栈顶出栈一个“”，如果“”的下标小于left的“（”的下标，那么返回false；如果大于，则left栈顶出栈，star栈顶出栈，进行下一轮比较；
    # 如果最后left还有值，star为空，返回false；如果left为空，star有值，返回true。
    left = []
    star = []
    for i in range(len(s)):
        if s[i] == "(":
            left.append(i)
        elif s[i] == "*":
            star.append(i)
        else:
            if left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False
    if not left:
        return True
    if left and not star:
        return False
    while left and star:
        l = left.pop()
        s = star.pop()
        if l < s:
            continue
        else:
            return False
    if left:
        return False
    return True

s="()()()((((()((()(()())(()))(())))((()((()())*(((())()))(()((())(((((((())()*)())((())*))))*)())()))"
print(checkValidString(s))