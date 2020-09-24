class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        # 节点的值+孩子节点的个数
        from collections import deque
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.pop()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for ch in node.children:
                queue.appendleft(ch)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        from collections import deque
        if not data:
            return
        # 转为列表
        data = list(map(int, data.split(",")))
        queue = deque()
        root = Node(data[0], [])
        queue.append([root, data[1]])
        i = 2
        while queue:
            node, num = queue.pop()
            for _ in range(num):
                tmp = data[i]
                i = i + 1
                tmp_num = data[i]
                i = i + 1
                tmp_node = Node(tmp, [])
                node.children.append(tmp_node)
                queue.appendleft([tmp_node, tmp_num])
        return root