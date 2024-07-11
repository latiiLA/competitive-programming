# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = [] # heap definition

        # Loop through the array and build the heap from the linked lists
        for arr in lists:
            while arr:
                heappush(heap, arr.val)
                arr = arr.next

        # incase linked list is empty return None, this is avoidable if dummy node is initialized to Null rather that to the head
        if len(heap) == 0:
            return None

        dummy = ListNode(heappop(heap))
        tail = dummy

        # while heap is not empty pop and add it to your linked list/dummy
        while heap:
            tail.next = ListNode(heappop(heap))
            tail = tail.next

        return dummy                