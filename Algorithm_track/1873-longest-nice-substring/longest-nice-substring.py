class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        unique_chars = set(s)
        n = len(s)
        
        
        for i in range(n):
            if s[i].upper() in unique_chars and s[i].lower() in unique_chars:
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])

            return left if len(left) >= len(right) else right
        
        

        return s