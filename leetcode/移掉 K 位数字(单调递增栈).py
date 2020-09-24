def removeKdigits(num, k) :
    stack = []
    n = len(num)
    remain = n - k
    if n == k:
        return "0"

    for digit in num:
        # 递增栈
        while k and stack and stack[-1] > digit:
            stack.pop()
            # 相当于删除一个
            k = k - 1
        stack.append(digit)
    if k == 0:
        return str(int(''.join(stack)))
    else:
        return str(int(''.join(stack[:remain])))