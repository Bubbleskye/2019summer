# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
# 找到所有长度为 n 的中心对称数。
#
# 示例 :
#
# 输入:  n = 2
# 输出: ["11","69","88","96"]

def findStrobogrammatic(n):
    selfmirror = ["0", "1", "8"]
    mirror = ["0", "1", "6", "8", "9"]
    if n == 1:
        return selfmirror
    dict = {}
    dict["0"] = "0"
    dict["1"] = "1"
    dict["6"] = "9"
    dict["9"] = "6"
    dict["8"] = "8"
    output = []

    def backtrack(s, count):
        # 从中间向两边生成数字
        if len(s) == count and s[0] != "0":
            output.append(s)
        if len(s) < count:
            for m in mirror:
                backtrack(m + s + dict[m], count)

    if n % 2 == 0:
        for m in mirror:
            count = n
            backtrack(m + dict[m], count)
    else:
        for m1 in selfmirror:
            for m2 in mirror:
                count = n
                backtrack(m2 + m1 + dict[m2], count)
    return output


n=2
print(findStrobogrammatic(n))
