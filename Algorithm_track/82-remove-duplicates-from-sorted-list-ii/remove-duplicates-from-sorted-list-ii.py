# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0, head)
        prev = dummy
        
        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev.next == current:
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = prev.next

        return dummy.next