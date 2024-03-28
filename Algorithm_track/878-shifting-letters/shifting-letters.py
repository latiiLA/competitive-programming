class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        prefix_sum = []
        prefix_sum.append(shifts[n - 1])

        # Calculate prefix sum of the the shifts
        for i in range(len(shifts) - 2, -1, -1):
            prefix_sum.append((prefix_sum[-1] + shifts[i]) % 26)

        letters = [0] * n

        # Calculate the value of the letters after shifts
        for i in range(n):
            letters[i] += (ord(s[i]) - 97 + prefix_sum[n - i - 1]) % 26 + 97
    
        return str("".join(chr(val) for val in letters))