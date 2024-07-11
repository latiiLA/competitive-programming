class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k # initilize k
        self.heap = [] # define heap 

        # loop through the number and build your heap. if the size becomes greater than k, pop
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)
        
    def add(self, val: int) -> int:
        # push the value to your heap, and pop if it becomes greater than k
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)