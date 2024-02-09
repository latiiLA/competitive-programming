class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        # word1= "".join([i for i in word1])
        # word2 = "".join([i for i in word2])

        return "".join([i for i in word1]) == "".join([i for i in word2])