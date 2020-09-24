# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 子树必须包含其所有后代，到叶子节点为止
# 二叉树的动态规划
# 参考打家劫舍3[valleft,numleft,booleft,maxval1,minval1]
# 每个节点存储【该节点的value，以这个节点为根节点的BTS树的节点数，是否是BTS树，以这个节点为根节点的树中最大值，以这个节点为根节点的树中最小值】
#
# 判断：1、左右子树都是BT树 2、左子树中最大值<根节点 3、右子树中最小值>根节点
# 后序遍历：左->右->根
class Solution:
    def largestBSTSubtree(root):
        if not root:
            return 0
        res = []

        # res中储存BTS树的节点数
        def helper(root):
            if not root:
                return [float("inf"), 0, True, -float("inf"), float("inf")]
            if not root.left and not root.right:
                res.append(1)
                return [root.val, 1, True, root.val, root.val]

            [valleft, numleft, booleft, maxval1, minval1] = helper(root.left)
            [valright, numright, booright, maxval2, minval2] = helper(root.right)

            if booleft and booright and (valleft == float("inf") or maxval1 < root.val) and (
                    valright == float("inf") or minval2 > root.val):
                res.append(1 + numleft + numright)
                maxvalue = max(root.val, maxval1, maxval2)
                minvalue = min(root.val, minval1, minval2)
                return [root.val, 1 + numleft + numright, True, maxvalue, minvalue]
            else:
                return [root.val, 1, False, -float("inf"), float("inf")]

        helper(root)
        return max(res)

