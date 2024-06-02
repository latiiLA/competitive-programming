class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""]  * 10 # NOT MORE THAN NINE MENTIONED IN THE DESCRIPTION
        separated_s = s.split(" ")  # Split the word
        print(separated_s)
        for word in separated_s:
            result[int(word[-1])] = word[:-1]

        ans = []
        for word in result:
            if word != '':
                ans.append(word)

        return " ".join(ans)