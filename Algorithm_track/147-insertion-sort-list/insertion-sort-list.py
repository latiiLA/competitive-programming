# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        current = head.next

        while current:
            if current.val > prev.val: # check if previous element is greater if it is continue, else search for its place
                prev, current = current, current.next
                continue
            
            temp = dummy
            while temp.next.val < current.val:
                temp = temp.next

            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current = prev.next

        return dummy.next
            