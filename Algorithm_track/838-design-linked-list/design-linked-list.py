class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return - 1

        current = self.head
        for i in range(index):
            current = current.next
        
        return current.val
            
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            current = self.head

            while current.next != None:
                current = current.next
            
            current.next = node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            node = Node(val)
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        elif index > 0 and index < self.size:
            current = self.head
            for i in range(index - 1):
                current = current.next
            
            current.next = current.next.next
            self.size -= 1
          
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)