# 请你写出一个能够举单词全部缩写的函数。
# 注意：输出的顺序并不重要。
#
# 示例：
# 输入: "word"
# 输出:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


# 对于这种某个元素选还是不选这样的情况，一般都用这样格式的回溯

word="word"
ans = []
def backtrace(i,cur, cnt):
    # 索引i 此时的字符cur i之前计数cnt
    if i == len(word):
        # 走到字符的末尾,加入结果中
        if cnt > 0:
            cur= cur +str(cnt)
        ans.append(cur)
    else:
        # 现在走到了索引为i的字符(从0开始),考虑cnt计数的字符要不要转成数字
        # 不转成数字,继续索引为i+1的字符，cnt计数+1,i索引+1
        backtrace(i+1,cur,cnt+1)
        # 转成数字,索引i+1,cnt置0 重新开始计数,cur+转成的数字+第i个字符(因为不可以数字连续)
        if cnt>0:
            backtrace(i + 1, cur + (str(cnt)) + word[i], 0)
        else:
            backtrace(i+1,cur+word[i],0)

backtrace(0,"",0)
print(ans)