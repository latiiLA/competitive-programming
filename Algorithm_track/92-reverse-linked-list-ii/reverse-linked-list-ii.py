# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        leftPrev, current = dummy, head
        for i in range(left - 1):
            leftPrev, current = current, current.next

        prev = None
        for i in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # merge the list
        leftPrev.next.next = current
        leftPrev.next = prev

        return dummy.next
