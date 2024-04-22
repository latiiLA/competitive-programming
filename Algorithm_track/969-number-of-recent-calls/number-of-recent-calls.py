class RecentCounter:

    def __init__(self):
        self.queue = []
        self.size = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.size += 1
        count = 0

        for i in range(self.size - 1, -1, -1):
            if self.queue[-1] - self.queue[i] <= 3000:
                count += 1
            else:
                break

        return count
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)