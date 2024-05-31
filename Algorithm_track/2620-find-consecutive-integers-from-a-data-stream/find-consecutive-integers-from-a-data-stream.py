class DataStream:

    def __init__(self, value: int, k: int):
        self.streams = deque()
        self.value = value
        self.dictionary = defaultdict(int) # keep track of the the count of k value from the 
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.streams.append(num)
        self.count += 1
        self.dictionary[num] += 1
        if self.count < self.k:
            return False

        if self.count > self.k:
            self.dictionary[self.streams.popleft()] -= 1
            self.count -= 1
        
        if self.dictionary[self.value] == self.k:
            return True
        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)