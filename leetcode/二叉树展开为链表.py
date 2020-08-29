# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return
    if not root.left and not root.right:
        return root
    if root.left and not root.right:
        root.right=root.left
        root.left=None
    else:
        tmp=root.right
        root.right=root.left
        p=root
        while p.right:
            p=p.right
        p.right=tmp
        root.left=None
    flatten(root.right)
    return root

# 递归 考虑左右子树组合的各种情况
# 对根节点处理完之后 再继续处理右节点即可，左节点已全为空