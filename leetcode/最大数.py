def largestNumber(nums):
    from functools import cmp_to_key
    # cmp_to_key()是将比较函数（comparison function）转化为关键字函数（key function）
    # 比较函数是可调用的，接受两个参数，比较这两个参数，例如：x,y 当x>y时返回1；等于时返回0；否则返回-1。
    # 关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值。
    # 采用cmp_to_key()函数，可以接受两个参数，将两个参数做处理，例如：作和 作差等，转换成一个参数，即可应用于关键字函数。
    def helper(x, y):
        if x + y > y + x:
            return -1
        # x排在y前面是当x+y>y+x的时候
        elif x + y < y + x:
            return 1
        else:
            return 0
    # 这道题有自己的排序规则，规则是 x + y > y + x，让x排在y前面。这里x,y表示任意两个数的字符串
    numss=map(str, nums)
    res=sorted(numss,key=cmp_to_key(helper))
    # sorted默认升序，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
    print(res)
    res = ''.join(res).lstrip('0')
    #  res不为空返回res，不然返回‘0’
    return res or '0'

nums=[3,30,34,5,9]
print(largestNumber(nums))