class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        index_of_words_containing_char = []

        # Looping through the list and finding if element has the string
        for i in range(len(words)):
            if x in words[i]:
                index_of_words_containing_char.append(i)
        
        return index_of_words_containing_char