class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        len_p = len(p)

        if n < len_p:
            return []

        # create dictionary for the anagram and the string 
        window_dict = defaultdict(int)
        anagram_dict = Counter(p)

        result = [] # list to return the result

        i = 0
        j = 0

        while j < len(p):
            window_dict[s[j]] += 1
            j += 1

        while j < n:
            if window_dict == anagram_dict:
                result.append(i)
            
            window_dict[s[j]] += 1
            window_dict[s[i]] -= 1

            if window_dict[s[i]] == 0:
                del window_dict[s[i]]

            i += 1
            j += 1

        if window_dict == anagram_dict:
                result.append(i)

        return result