"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        chead=head
        while chead:
            copynode=Node(chead.val,None,None)
            copynode.next=chead.next
            chead.next=copynode
            chead=copynode.next
        chead2=head
        while chead2:
            tmp=chead2.next
            if chead2.random:
                tmp.random=chead2.random.next
            chead2=tmp.next
        chead3=head
        res=head.next
        while chead3.next:
            tmp = chead3.next
            chead3.next = tmp.next
            chead3 = tmp
        return res