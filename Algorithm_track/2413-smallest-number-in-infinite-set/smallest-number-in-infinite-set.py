class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heappush(self.heap, 1)
        self.current = 1
        self.discarded = set()

    def popSmallest(self) -> int:
        if self.heap:
            popped = heappop(self.heap)
            self.discarded.add(popped)
            if popped == self.current:
                self.current += 1
                heappush(self.heap, self.current)
                
            return popped

    def addBack(self, num: int) -> None:
        if num in self.discarded:
            heappush(self.heap, num)
            self.discarded.remove(num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)