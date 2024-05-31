class DataStream:

    def __init__(self, value: int, k: int):
        self.streams = []
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.streams.append(num)
            if len(self.streams) >= self.k:
                return True
            return False
        else:
            self.streams = []
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)