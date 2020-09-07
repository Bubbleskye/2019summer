# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # 存储以各个结点为根节点时的最大路径值
        self.d=[]
    def diameterOfBinaryTree(self,root):
        if not root:
            return 0
        def diameter(root):
            if not root:
                self.d.append(-1)
                return [-1,-1]
            elif not root.left and not root.right:
                self.d.append(0)
                return [0,0]
            else:
                [lleft,lright]=diameter(root.left)
                [rleft,rright]=diameter(root.right)
                self.d.append(max(lleft,lright)+1+max(rleft,rright)+1)
                # 左右连接到根节点还有两个1
                return [max(lleft,lright)+1,max(rleft,rright)+1]
        diameter(root)
        return max(self.d)
    # 遍历二叉树，每个二叉树的节点储存【左子树最长路径，右子树最长路径】