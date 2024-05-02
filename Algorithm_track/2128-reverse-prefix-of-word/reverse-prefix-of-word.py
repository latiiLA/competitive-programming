class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        i = 0
        flag = False
        while i < len(word):
            if word[i] == ch:
                flag = True
                break
            else:
                i += 1

        if not flag:
            return word
        
        return word[:i+1][::-1] + word[i + 1:]