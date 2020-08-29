array=[2,4,3,6,3,2,5,5]
# 进行分组，两个只出现一次的数字在不同的组中；相同的数字会被分到相同的组中
sum = 0
for num in array:
    sum = sum ^ num
# 记这两个只出现了一次的数字为 a 和 b，那么所有数字异或的结果就等于 a 和 b 异或的结果，我们记为 x。
# x的每一位意味着如果我们把 a 和 b 写成二进制的形式，各个位之间的关系：相同为0，不同为1
# 以x为1的一位进行分组,肯定满足分组的要求
# print(sum)
wit = 0
while sum & 1 != 1:
    sum = sum >> 1
    wit = wit + 1
# 得到sum的第wit位是1/1=000001 除了末位 其余&之后都是0
array1 = []
array2 = []
for num in array:
    if (num >> wit) & 1 == 1:
        array1.append(num)
    else:
        array2.append(num)
sum1 = 0
for num1 in array1:
    sum1 = sum1 ^ num1
sum2 = 0
for num2 in array2:
    sum2 = sum2 ^ num2
print(sum1, sum2)
