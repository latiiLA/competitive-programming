class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = sorted(s)
        t = sorted(t)

        # compares the sorted strings and if they are not the same or if we finish scanned through s return the last element of j
        for i in range(len(t)):
            if i == len(s) or t[i] != s[i]:
                return t[i]