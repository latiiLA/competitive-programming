class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        result = list(s)
        letters = []
        positions = []

        # record the vowels and their positions
        for i in range(len(s)):
            if s[i] in vowels:
                positions.append(i)
                letters.append(s[i])

        letters.sort()

        # replace the sorted vowels in their place
        i = 0
        for pos in positions:
            result[pos] = letters[i]
            i += 1
        print(result)

        return "".join(result)
                       