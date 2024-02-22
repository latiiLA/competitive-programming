class FrequencyTracker:

    def __init__(self):
        self.frequencyTracker = defaultdict(int) # hash map to track dictionary value 
        self.frequencyMap = defaultdict(int)

    def add(self, number: int) -> None:
        self.frequencyTracker[number] += 1     
        f = self.frequencyTracker[number]
        self.frequencyMap[f] += 1
        self.frequencyMap[f - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.frequencyTracker[number] > 0:
            self.frequencyTracker[number] -= 1
            f = self.frequencyTracker[number]
            self.frequencyMap[f] += 1
            self.frequencyMap[f+1] -= 1
    
    def hasFrequency(self, frequency: int) -> bool:
        if self.frequencyMap[frequency] > 0:
            return True


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)