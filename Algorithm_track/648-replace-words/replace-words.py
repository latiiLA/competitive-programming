class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        sentence = sentence.split(" ")
        for word in sentence:
            prefix = word
            for i in range(len(word) + 1):
                if word[:i] in dictionary:
                    prefix = word[:i]
                    break
            result.append(prefix)
                

        return " ".join(result)