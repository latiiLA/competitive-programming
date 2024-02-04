class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged_word = ""
        i = 0
        
        # creates a merged word upto the minimum length word
        while i < min(len(word1), len(word2)):
            merged_word += word1[i]
            merged_word += word2[i]
            i += 1
        
        # Adds elements that are not added from the word having maximum length
        while i < max(len(word1), len(word2)):
            if len(word1) > len(word2):
                merged_word += word1[i]
            else:
                merged_word += word2[i]
            i += 1

        return merged_word



                
