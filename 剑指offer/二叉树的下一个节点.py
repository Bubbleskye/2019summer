class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
def GetNext(pNode):
    # write code here
    if not pNode:
        return None
    if pNode.right:
        tmp = pNode.right
        while tmp.left:
            tmp = tmp.left
        return tmp
    while pNode.next:
        tmp = pNode.next
        if tmp.left == pNode:
            return tmp
        pNode = tmp
    return None