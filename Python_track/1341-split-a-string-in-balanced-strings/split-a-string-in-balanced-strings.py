class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0

        for j in s:
            if j == "R":
                count += 1
            if j == "L" :
                count -= 1
            if count == 0:
                balance += 1

        return balance 