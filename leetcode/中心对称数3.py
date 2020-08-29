# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
# 写一个函数来计算范围在 [low, high] 之间中心对称数的个数。
#
# 示例:
#
# 输入: low = "50", high = "100"
# 输出: 3
# 解释: 69，88 和 96 是三个在该范围内的中心对称数

class Solution:
    def __init__(self):
        self.count=0
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        selfmirror = ["0", "1", "8"]
        mirror = ["0", "1", "6", "8", "9"]
        dict = {}
        dict["0"] = "0"
        dict["1"] = "1"
        dict["6"] = "9"
        dict["9"] = "6"
        dict["8"] = "8"
        nlow=len(low)
        nhigh=len(high)
        low=int(low)
        high=int(high)
        def backtrack(s, n):
            if len(s) == n and s[0]!="0" and int(s)>=low and int(s)<=high:
                self.count=self.count+1
            if len(s) < n:
                for m in mirror:
                    backtrack(m + s + dict[m], n)
        for n in range(nlow,nhigh+1):
            if n % 2 == 0:
                for m in mirror:
                    backtrack(m + dict[m], n)
            else:
                if n==1:
                    for m1 in selfmirror:
                        if int(m1)>=low and int(m1)<=high:
                            self.count=self.count+1
                else:
                    for m1 in selfmirror:
                        for m2 in mirror:
                            backtrack(m2 + m1 + dict[m2], n)
        return self.count
