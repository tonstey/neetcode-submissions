# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryBit = 0
        head = curr = ListNode()

        while l1 and l2:
            curr.next = ListNode(val=(l1.val +l2.val + carryBit) % 10)
            carryBit = 0
            if l1.val + l2.val >= 10:
                carryBit = 1
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            curr.next = ListNode(val=(l1.val + carryBit) % 10)
            
            if l1.val + carryBit >= 10:
                carryBit = 1
            else:
                carryBit = 0
            l1 = l1.next
            curr = curr.next
        while l2:
            curr.next = ListNode(val=(l2.val + carryBit) % 10)
   
            if l2.val + carryBit >= 10:
                carryBit = 1
            else:
                carryBit = 0
            l2 = l2.next
            curr = curr.next

        if carryBit == 1:
            curr.next = ListNode(val=1)


        return head.next
        