class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n:
            return ""

        tDictionary = Counter(t)
        windowDictionary = Counter()

        i = 0
        j = 0

        result = float('inf')
        string_result = [0, 0]

        while j < n:
            windowDictionary[s[j]] = windowDictionary.get(s[j], 0) + 1
           
            while all(key in windowDictionary and windowDictionary[key] >= value for key, value in tDictionary.items()):
                if result > j - i + 1:
                    result = j - i + 1
                    string_result[0] = i
                    string_result[1] = j + 1

                
                windowDictionary[s[i]] -= 1
                if windowDictionary[s[i]] == 0:
                    del windowDictionary[s[i]]
                i += 1
           
            j += 1
        return s[string_result[0]:string_result[1]] if result != float('inf') else ""