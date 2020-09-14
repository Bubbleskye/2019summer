# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        fast=head.next
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        slow.next=None
        left= self.sortList(head)
        right= self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right=right.next
            h = h.next
        if left :
            h.next = left
        else :
            h.next = right
        return res.next