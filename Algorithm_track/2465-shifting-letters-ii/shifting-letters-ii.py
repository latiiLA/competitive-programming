class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)

        # calculate the shifts and create a list of their effects
        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                prefix[shifts[i][0]] += 1
                prefix[shifts[i][1] + 1] -= 1
            else:
                prefix[shifts[i][0]] -= 1
                prefix[shifts[i][1] + 1] += 1

        # create a prefix list of the sum of shifts
        for i in range(1, len(prefix)):
            prefix[i] = (prefix[i - 1] + prefix[i]) % 26

        # calculate the result of the shifts
        result = []
        for i in range(n):
            result.append(chr((ord(s[i]) - 97 + prefix[i]) % 26 + 97))
        
        return "".join(result)
