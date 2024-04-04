class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n + 1)

        vowels = {"a": "a", "e": "e", "i": "i", "o": "o", "u": "u"}

        # create a prefix sum of the words that satisfy the condition at every index
        for i in range(n):
            prefix[i + 1] = prefix[i] + (words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels)

        result = []

        # loop through the query and find the result by looking at the prefix sum
        for i in range(len(queries)):
            result.append(prefix[queries[i][1] + 1] - prefix[queries[i][0]])

        return result
