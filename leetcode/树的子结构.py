# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A, B):
        # 比对两棵树其他的节点是否相同
        def isSame(root1,root2):
            if not root2:
                return True
            elif not root1:
                return False
            elif root1.val!=root2.val:
                return False
            else:
                return isSame(root1.left,root2.left) and isSame(root1.right,root2.right)

        res=False
        # 在A树中寻找与B树根节点相同的节点
        if A and B:
            if A.val==B.val:
                res=isSame(A,B)
            if not res:
                res=self.isSubStructure(A.left,B)
            if not res:
                res=self.isSubStructure(A.right,B)
        return res