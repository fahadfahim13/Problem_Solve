from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    bh_h = ListNode()
    bh = bh_h
    ah_h = ListNode()
    ah = ah_h

    while head != None:
        if head.val < x:
            bh.next = head
            bh = bh.next
        else:
            ah.next = head
            ah = ah.next
        head = head.next
    ah.next = None
    bh.next = ah_h.next
    return bh_h.next


