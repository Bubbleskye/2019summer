# 如何判断一个字符串改变K个字符，能够变成一个连续串:如果当前字符串中的出现次数最多的字母个数+K大于串长度，那么这个串就是满足条件的
# historyCharMax保存滑动窗口内相同字母出现次数的历史最大值
# 通过判断窗口宽度(right - left + 1)是否大于historyCharMax + K，大于则窗口滑动，否则窗口就扩张
def characterReplacement(s,k):
    map=[0 for _ in range(26)]
    if not s:
        return 0
    left=0
    right=0
    historymax=0
    maxlen=0
    while right<len(s):
        index=ord(s[right])-ord('A')
        map[index]=map[index]+1
        historymax=max(historymax,map[index])
        if right-left+1>historymax+k:
            map[ord(s[left])-ord('A')]=map[ord(s[left])-ord('A')]-1
            left=left+1
            right=right+1
        else:
            maxlen=max(maxlen,right-left+1)
            right=right+1
    return maxlen