# 一个节点的状态有[是否被监控，是否放置相机]
# 贪心算法：在每个节点上尽可能不放置监控
# 仅当所遍历的节点的任一子节点未被监控时，当前节点必须放置监控，否则子节点将无法被监控
# 其余情况，节点首先考虑不放监控

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=0
    def minCameraCover(self, root):
        def helper(root):
            if not root:
                return [True, False] # 对于空，自身是被监控的，且自身没有放置
            [watchl, placel] = helper(root.left)
            [watchr, placer] = helper(root.right)
            if watchl and watchr:
            # 如果左右节点都被监控了，那该节点就不需要放置
                place = False
            else:
                place = True
            if placel or placer or place:
            # 如果左节点、右节点或该节点放置了，那该节点就被监控了
                watch = True
            else:
                watch=False
            if place:
                self.ans = self.ans + 1 # 如果该节点需要放置，则总数量+1
            return [watch,place]

        [watch,place] = helper(root)
        if watch:
            return self.ans
        else:
            return self.ans+1 # 最后还需判断一下根节点是否被监控，没有被监控的话根节点也需要放置