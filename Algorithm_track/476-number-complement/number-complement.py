class Solution:
    def findComplement(self, num: int) -> int:
        complement = deque()

        while num > 0:
            comp = "1" if num&1 == 0 else "0"
            complement.appendleft(comp)
            num >>= 1

        return int("".join(complement), 2)