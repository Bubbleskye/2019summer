# 虽然是全排列 但不能用回溯法 会超时
# 我们发现当首数字确定了,后面和首数字组成数字的个数相等的!
# 比如: 首数字为1,后面有组成两个数123,132,可以组成2个数.当首数字为2,3同样都是.
# 所有我们要找k = 3的数字 ,我们只需要 3/2 便可找到首数字什么
import math
n=3
k=2
num = [str(i) for i in range(1, n+1)]
res = ""
while n > 0:
    n=n-1
    t = math.factorial(n)
    # factorial整数的阶乘:n!=1×2×3×...×n
    # 即以每个字母为开头有t个排列
    loc = math.ceil(k / t) - 1
    res = res+ num[loc]
    # 求出第k个排列的此时子序列首字母为num[loc]
    num.pop(loc)
    k = k % t
    # 求出第k个排列在以num[loc]为开头的排列组合中的第几个(从1开始) 0对应最后一个
print(res)