class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        n = len(word)
        vowels = {"a", "e", "i", "o", "u"}
        beautiful = {c: 0 for c in vowels}

        i = 0
        j = 1

        result = 0

        beautiful[word[0]] = 1

        while i < n:
            if word[i] != 'a': # this improves the time complexity
                i += 1
                continue
            j = i + 1
            beautiful = {c: 0 for c in vowels}
            beautiful[word[i]] += 1
            while j < n and word[j] >= word[j - 1]:
                beautiful[word[j]] += 1
                j += 1

            if all(count > 0 for count in beautiful.values()):
                result = max(result, j - i)
                print(i, j, result)

            else:
                beautiful = {c: 0 for c in vowels}
                
            i = j

        return result

                    

            