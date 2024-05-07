# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # There are various options to solve this problem
        # This approach involves applying queue and converting that back to list
        stack = []
        current = head
        carry = 0

        while current:
            stack.append(current.val)
            current = current.next

        queue = deque()
        while stack:
            num = stack[-1] * 2 + carry
            carry = num // 10
            queue.appendleft(num % 10)
            stack.pop()
        if carry:
            queue.appendleft(carry)

        dummy = ListNode()
        current = dummy
        while queue:
            node = ListNode(queue.popleft())
            current.next = node
            current = current.next
        
        return dummy.next

            
        
