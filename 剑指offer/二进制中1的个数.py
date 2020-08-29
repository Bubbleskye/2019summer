def NumberOf1(n):
    # write code here
    if n < 0:
        n = n & 0xffffffff
    count = 0
    while n:
        n = (n - 1) & n
        count = count + 1
    return count

print(NumberOf1(-1))