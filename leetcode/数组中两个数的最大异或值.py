# 异或运算的性质
# 解决这个问题，我们首先需要利用异或运算的一个性质：
# 如果 a ^ b = c 成立，那么a ^ c = b 与 b ^ c = a 均成立。
# 即 如果有三个数，满足其中两个数的异或值等于另一个值，那么这三个数的顺序可以任意调换。
# 异或运算其实就是 二进制下不进位的加法

def findMaximumXOR(nums):
    res = 0
    mask = 0
    for i in range(30, -1, -1):
        # 二进制最多31位 0-30 从最高位开始
        mask = mask | (1 << i)
        # 通过左移1，mask表示前缀是前31-i位全是1
        # 在下面的&中，保留指定位的数字（1&n=n 0&n=0）
        # s中存储nums中各个数字前31-i位的值
        s = set()
        for num in nums:
            s.add(mask & num)

        # 先“贪心地”假设这个数位i上是 “1”,其余的位的值遵循之前得到的res的前缀
        temp = res | (1 << i)
        # s中两个数i^j=1 根据异或的性质有j=1^i
        # 如果全部前缀都看完，都不符合条件，这个数位上就是 “0”
        for prefix in s:
            if temp ^ prefix in s:
                res = temp
                break
    return res

nums=[3,10,5,25,2,8]
print(findMaximumXOR(nums))