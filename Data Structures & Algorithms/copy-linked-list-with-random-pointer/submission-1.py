"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        
        copyHead = copyCurr = Node(0)
        
        mapping = {}
        
        while curr:
            copyCurr.next = Node(x=curr.val )
            mapping[curr] = copyCurr.next

            copyCurr = copyCurr.next
            curr = curr.next
            
        copyCurr = copyHead.next
        curr = head

        while curr:
            copyCurr.random = mapping.get(curr.random, None)

            copyCurr = copyCurr.next
            curr = curr.next


        return copyHead.next