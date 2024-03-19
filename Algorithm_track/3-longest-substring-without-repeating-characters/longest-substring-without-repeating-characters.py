class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_substring = 0
        start = 0

        dictionary = {}

        # Add if the character is new. if not calculate the length max substring
        for i in range(n):
            if s[i] in dictionary:
                start = max(start, dictionary[s[i]] + 1)

            max_substring = max(max_substring, i - start + 1)
            dictionary[s[i]] = i            
                
        return max_substring
            