def canWin(self, s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] == "+" and s[i + 1] == "+" and not self.canWin(s[0:i] + "--" + s[i + 2:]):
            return True
    return False

# 递归求解
# 上一步（对手）一定是Flase