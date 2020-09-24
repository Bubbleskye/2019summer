# 反向中序遍历 右—>根—>左
class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val = root.val + self.sum
            self.sum = root.val
            dfs(root.left)
            return root

        return dfs(root)