# 给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。
# 如果可以找到返回 True，否则返回 False。
# 输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
# 输出：true
# 解释：2 加 3 和为 5 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        self.ans = False

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False

        # 先序遍历第一棵树，找到相对于target，此时另一个值，存入self.res
        def preorder(root, target):
            if not root:
                return self.res
            self.res.append(target - root.val)
            preorder(root.left, target)
            preorder(root.right, target)

        preorder(root1, target)

        # 先序遍历第二棵树，是否值在self.res中
        def preorder2(root):
            if not root:
                return
            if root.val in self.res:
                self.ans = True
            preorder2(root.left)
            preorder2(root.right)

        preorder2(root2)
        return self.ans