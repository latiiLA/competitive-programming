# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maximum_pair = 0
        # Separate the first and the second list
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        current = slow.next
        slow.next = None

        # Reverse the second list      
        prev = None       
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # move and find the maximum pair
        first = head
        second = prev
        while first:
            maximum_pair = max(maximum_pair, first.val + second.val)
            first = first.next
            second = second.next        
        
        return maximum_pair