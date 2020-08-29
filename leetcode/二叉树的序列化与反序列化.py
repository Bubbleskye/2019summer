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
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp != "null":
                    res.append(tmp.val)
                    if tmp.left:
                        queue.append(tmp.left)
                    else:
                        queue.append("null")
                    if tmp.right:
                        queue.append(tmp.right)
                    else:
                        queue.append("null")
                else:
                    res.append("null")

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        length = len(data)
        if not length:
            return None
        # 两个列表分别存放parents和child
        root = TreeNode(data[0])
        parents = [root]
        childs = []
        i = 1
        while i < length:
            for parent in parents:
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.left = node
                    childs.append(node)
                i += 1
                # 加左节点
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.right = node
                    childs.append(node)
                i += 1
            #     加右节点

            if childs:
                parents = childs
                childs = []
        return root