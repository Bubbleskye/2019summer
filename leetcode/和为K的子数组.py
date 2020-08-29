def subarraySum(nums, k) :
    # 连续子数组用前缀和
    if not nums:
        return 0
    P = [0]
    for n in nums:
        P.append(P[-1] + n)
    P = P[1:]

    res = 0
    dict = {}
    for i in range(len(P)):
        if P[i] - k in dict.keys():
            res = res + dict[P[i] - k]
        if P[i] ==k:
            res=res+1
        if P[i] not in dict:
            dict[P[i]] = 1
        else:
            dict[P[i]] = dict[P[i]] + 1
    return res
nums=[1,1,1]
k=2
print(subarraySum(nums, k))