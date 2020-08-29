def trailingZeroes(n):
    # 2*5=10，所有的零都是由此而来
    # 而5比2出现的概率低，所以考虑5的个数
    # 每5个数，出现一次5；每25个数多出来一个5；每125个数多出现2个5......
    cnt = 0
    i = 1
    while n // pow(5, i) > 0:
        cnt = cnt + n // pow(5, i)
        i = i + 1
    return cnt