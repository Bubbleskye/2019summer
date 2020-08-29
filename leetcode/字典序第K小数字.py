# 其实就是先序遍历十叉树到第k个节点
# 但是不需要用前序遍历，通过数学方法求出节点1和节点2之间需要走几步，减少很多没必要的移动。走几步即节点2之前有几个点.
# 判断当前节点下一共有多少个子节点，记为N。判断N与剩余步数K的关系。
# 如果N>=K，证明要找的数字在这个节点下面，就往下走。如果N<K，证明要找的数不在当前节点下面，往右走。
def findKthNumber(n,k):
    def cal_steps(n, n1, n2):
        step = 0
        #  当前的前缀当然不能大于上界
        while n1 <= n:
            step = step + min(n2, n + 1) - n1
            # min(n2,n+1) n2是满二叉树的情况下
            # n+1是非满二叉树的情况,假若现在上界 n为 12，算出以 1 为前缀的子节点数，首先 1 本身是一个节点，
            # 接下来要算下面 10，11，12，一共有 4 个子节点。如果是12-10则是两个,加上1是三个,12被认成了第三个节点,所以要+1
            n1 *= 10
            n2 *= 10
        return step

    cur = 1
    k = k - 1

    while k > 0:
        steps = cal_steps(n, cur, cur + 1)
        if steps <= k:
            # 目标值不在当前前缀下
            # steps中包括cur这个点有steps个值,但是cur这个点之前已经被减掉了
            # 所以即使steps==k,在现在这个前缀下的点数是少于k的,所以不在当前前缀下
            cur = cur + 1
            k = k - steps

        else:
            # 目标值在当前前缀下
            cur = cur * 10
            k = k - 1


    return cur


res=findKthNumber(12,4)
print(res)