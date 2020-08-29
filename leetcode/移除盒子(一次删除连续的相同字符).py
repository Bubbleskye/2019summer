# dp[l][r][k]为起始下标l，结束下标r，k表示在下标r后面紧接着有k个元素值和boxes[r]相同，的最大积分和、
# 比如[l,l+1,···,r-1,r,值同r，值同r，值同r]
# 这里有3个元素和boxes[r]相同，即k==3，那么dp[l][r][3]=dp[l][r-1][0]+4*4  因为有3个和[r]相同，即可以消除4个所以加上4*4
# 得到初始化条件dp[l][r][k]=dp[l][r-1][0]+(k+1)*(k+1)
# 但是有可能在boxes[l]~boxes[r-1]中也存在和boxes[r]相同值的元素，有可能获得更大的积分和
# 比如[l,l+1,···,i,···,r-1,r,值同r，值同r，值同r]，假设boxes[i]==boxes[r]
# 那么可能先移除boxes[i+1]~boxes[r-1]，这样就能使原来的dp[l][r][3]的k=3变的更大，但是r变得更小，但是积分和更大
# 因此就需要在boxes[l]~boxes[r-1]中找到boxes[i]==boxes[r]
# 这样子先移除boxes[i+1]~boxes[r-1]，这一部分的最大积分和是dp[i+1][r-1][0]
# 移除之后是[l,l+1,···,i,值同i(原来是r)，值同i(原来是r+1)，值同i(原来是r+2)，值同i(原来是r+3)]
# 剩下这部分是dp[l][i][k+1]
# 总和起来就是dp[l][r][k]=max(dp[l][r][k],dp[i+1][r-1][0]+dp[l][i][k+1])
# 最后的答案就是dp[0][boxes.size()-1][0]

def removeBoxes(boxes):
    memo = {}

    def dp(l, r, k):
        if l > r:
            return 0
        if (l, r, k) in memo:
            return memo[(l, r, k)]
        while r > l and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1
        res = dp(l, r - 1, 0) + (k + 1) * (k + 1)

        for i in range(l, r):
            if boxes[i] == boxes[r]:
                res = max(res, dp(i + 1, r - 1, 0) + dp(l, i, k + 1))

        memo[(l, r, k)] = res
        return res

    return dp(0, len(boxes) - 1, 0)