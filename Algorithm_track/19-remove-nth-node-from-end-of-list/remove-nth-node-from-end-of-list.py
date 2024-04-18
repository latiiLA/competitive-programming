# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
             
        dummy = ListNode(0, head)
        left = dummy

        n = length - n
        for i in range(n):
            left = left.next
        
        left.next = left.next.next
        return dummy.next