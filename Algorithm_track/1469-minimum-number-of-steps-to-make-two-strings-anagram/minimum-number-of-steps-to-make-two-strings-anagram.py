class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_list = list(s)
        t_list = list(t)
        
        s_list.sort()
        counter = Counter(s_list)
        t_list.sort()
        count = 0

        for i in range(len(t)):
            if t[i] in counter:
                counter[t[i]] -= 1
                if counter[t[i]] == 0:
                    del counter[t[i]]
            else:
                count += 1 

        return count
