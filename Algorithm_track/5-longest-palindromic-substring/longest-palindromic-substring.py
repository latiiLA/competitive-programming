class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = (0, 0)

        for i in range(n):
            l = r = i

            while l >= 0 and r < n and s[l] == s[r]:
                if result[1] - result[0] < r - l:
                    result = (l, r)
                l -= 1
                r += 1

            # for even
            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                if result[1] - result[0] < r - l:
                    result = (l, r)
                l -= 1
                r += 1

        return s[result[0]:result[1] + 1]
