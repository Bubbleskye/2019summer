def GetFragment(str):
    LEN = len(arr)
    SUM = [0]
    for i in range(LEN):
        SUM.append(SUM[i] + arr[i])
    res = k
    for i in range(LEN):
        if i + res > LEN:
            break
        for j in range(i + res, LEN + 1):
            if SUM[j] - SUM[i] + k < j - i:
                break
            if SUM[j] - SUM[i] + k >= j - i:
                res = max(res, j - i)
    return res