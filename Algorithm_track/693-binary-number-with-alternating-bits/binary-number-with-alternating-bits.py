class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)
        result = True

        # loop through the binary of the number and check if consequetive bits are the same
        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                result = False
                break

        return result
