class Solution:
    def partitionString(self, s: str) -> int:
        result = []
        temp = []
        for char in s:
            if char not in temp:
                temp.append(char)
            else:
                result.append("".join(temp))
                temp = []
                temp.append(char)
        
        if len(temp) > 0:
            return len(result) + 1
            
        return len(result)
            