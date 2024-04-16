# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head     

        # find the middle element to divide the list by using fast and slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow)
        # print(fast)        
       
        # reverse one of the half to make the comparison easy
        fastReversed = None
        while slow:
            nextNode = slow.next
            slow.next = fastReversed
            fastReversed = slow
            slow = nextNode
            
        
        # compare both half if they are palindrome or not
        slow = head
        fast = fastReversed
        # print(slow)
        # print(fast)
        while slow and fast:
            if slow.val != fast.val:
                return 0
            slow = slow.next
            fast = fast.next
        
        return 1
