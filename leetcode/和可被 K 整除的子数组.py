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
        P.append((P[-1] + x) % K)
    P = P[1:]
    count = Counter(P)
    res=0
    for v in count.values():
        res=res+v * (v - 1) // 2
    res=res+count.get(0,0)
    return res
A=[4,5,0,-2,-3,1]
K=5
print(subarraysDivByK(A, K))