# 通常，涉及连续子数组问题的时候，我们使用前缀和来解决。
# 我们令 P[i] = A[0] + A[1] + ... + A[i]。
# 那么，每个连续子数组的和 sum(i, j) 就可以写成 P[j] - P[i-1] （其中 j > i 且 i > 0） 的形式。
# 那么判断子数组的和能否被 K 整除就可以写成 (P[j] - P[i-1])%K == 0，根据同余定理只要 P[j]%K == P[i-1]%K，就可以保证上面的式子成立。
def subarraysDivByK(A, K):
    from collections import Counter
    if not A:
        return 0
    P = [0]
    for x in A:
        P.append((P[-1] + x))
    P = P[1:]
    # print(P)
    dict = {}
    res = 0
    for i in range(len(P)):
        if P[i] % K == 0:
            res = res + 1
            if P[i] % K in dict:
                res = res + dict[P[i] % K]
        elif P[i] % K in dict:
            res = res + dict[P[i] % K]
        if P[i] % K not in dict:
            dict[P[i] % K] = 1
        else:
            dict[P[i] % K] = dict[P[i] % K] + 1
    return res

A=[4,5,0,-2,-3,1]
K=5
print(subarraysDivByK(A, K))