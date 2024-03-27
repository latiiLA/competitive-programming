class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0]

        for i in range(len(self.numbers)):
            prefix.append(prefix[-1] + self.numbers[i])

        return prefix[right + 1] - prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)