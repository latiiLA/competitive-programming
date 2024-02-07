class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0

        for sentence in sentences:
            counter = 1
            for sent in sentence:
                if sent == " ":
                    counter += 1
            count = max(count, counter)

        return count 