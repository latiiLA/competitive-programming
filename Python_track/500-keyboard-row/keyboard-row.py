class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []

        # Checks if every character of a word is in one of the row strings
        for word in words:
            if all(char in row1 for char in word.lower()) or all(char in row2 for char in word.lower()) or all(char in row3 for char in word.lower()):
                result.append(word)
          
        return result
                        
