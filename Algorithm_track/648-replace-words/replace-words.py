class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        sentence = sentence.split(" ")
        for word in sentence:
            flag = False
            for i in range(len(word)):
                if word[:i] in dictionary:
                    result.append(word[:i])
                    flag = True
                    break
            if not flag:
                result.append(word)
                

        return " ".join(result)