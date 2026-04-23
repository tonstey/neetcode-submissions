# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        prev, curr = None, head
        end = head

        for i in range(n-1):
            end = end.next

        while end.next:
            prev = curr
            curr = curr.next
            end = end.next

        if curr == head:
            return head.next

        prev.next = curr.next

        return head

        