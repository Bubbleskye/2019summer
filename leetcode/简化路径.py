def simplifyPath(path):
    stack = []
    path = path.split("/")
    # split通过指定分隔符"/"对字符串进行切片

    for i in path:
        if i == '..':
            if stack:
                stack.pop()
        elif i and i != '.':  # i的作用是规避空字符串，因为可能原path存在'////'多个斜杠的情况，split后会产生大量空集
            stack.append(i)

    return '/' + '/'.join(stack)  # 本句为精髓，因为仅允许一个'/'进行分隔，且开头需要用一个'/'作为起点

path="/a/./b/../../c/"
print(simplifyPath(path))