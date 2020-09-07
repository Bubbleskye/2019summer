# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 写一个函数conutS统计该根节点下有多少结点
# 从而得到根节点的所在位置，进而递归继续在左子树或右子树中寻找。
# 当找到根节点满足k，输出。

def kthSmallest(root, k):
    if not root:
        return

    def conutS(root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left and root.right:
            return 1+conutS(root.right)
        elif root.left and not root.right:
            return 1+conutS(root.left)
        else:
            return 1+conutS(root.left)+conutS(root.right)

    count=conutS(root.left)
    if count>k-1:
        return kthSmallest(root.left,k)
    elif count==k-1:
        return root.val
    else:
        return kthSmallest(root.right,k-count-1)