def rob(root) -> int:
    if not root:
        return 0

    def helper(node):
        if not node:
            return [0, 0]
        [noleft, left] = helper(node.left)
        [noright, right] = helper(node.right)
        return [max(left, noleft) + max(right, noright), noleft + noright + node.val]

    [noroot, root] = helper(root)
    return max(noroot, root)

# 任何一个节点能偷到的最大钱的状态可以定义为
# 当前节点选择不偷: 当前节点能偷到的最大钱数 = 左孩子能偷到的最大钱 + 右孩子能偷到的最大钱
# root[0] = max(rob(root.left)[0], rob(root.left)[1]) + max(rob(root.right)[0], rob(root.right)[1])
# 当前节点选择偷: 当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
# root[1] = rob(root.left)[0] + rob(root.right)[0] + root.val;