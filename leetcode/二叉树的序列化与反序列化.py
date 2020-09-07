# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        from collections import deque
        queue = deque()
        queue.append(root)
        res.append(root.val)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append("null")
                if node.right:
                    queue.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append("null")
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        from collections import deque
        queue = deque()
        queue.append(root)
        i = 1
        while queue and i < len(data):
            node = queue.popleft()
            if data[i] != "null":
                node.left = TreeNode(data[i])
                queue.append(node.left)
            else:
                node.left = None
            i = i + 1
            if data[i] != "null":
                node.right = TreeNode(data[i])
                queue.append(node.right)
            else:
                node.right = None
            i = i + 1
        return root
