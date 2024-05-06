class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # there are three parts if k == n or less n or greater than n. depending on that create approppriate condition
        if n == 1:
            return "0"
        mid = 2 ** n / 2

        if k < mid:
            return str(self.findKthBit(n-1, k))
        elif k == mid:
            return "1"
        else:
            return str(1 - int(self.findKthBit(n - 1, mid - (k - mid))))