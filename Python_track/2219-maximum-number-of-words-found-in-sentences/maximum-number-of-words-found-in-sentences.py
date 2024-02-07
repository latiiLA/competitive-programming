class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0

        # Looping through the sentences and find the maximum length
        for sentence in sentences:
            count = max(count, len(sentence.split(" ")))
        
        return count 