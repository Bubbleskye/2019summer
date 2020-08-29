class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def reConstructBinaryTree(pre, tin):
    # write code here
    if len(pre) == 0:
        return None
    root = TreeNode(pre[0])
    index = tin.index(pre[0])
    root.left = reConstructBinaryTree(pre[1:index + 1], tin[0:index])
    root.right =reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
    return root

pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6]
root=reConstructBinaryTree(pre, tin)