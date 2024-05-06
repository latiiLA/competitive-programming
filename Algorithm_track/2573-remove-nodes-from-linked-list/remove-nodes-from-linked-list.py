# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        # Use monotonic stack to solve the question
        current = head
        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()
            stack.append(current)
            current = current.next
        
        # Connect back the results of the stack
        result = None
        while stack:
            current = stack.pop()
            current.next = result
            result = current

        return result