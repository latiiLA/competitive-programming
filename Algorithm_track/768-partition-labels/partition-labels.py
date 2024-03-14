class Solution:
    def partitionLabels(self, s: str) -> List[int]:
     
        partition = {}
        result = []

        n = len(s)

        # create a dictionary
        for i in range(n):
            partition[s[i]] = i

        partitionIndex = partition[s[0]]
        start = 0

        for i in range(0, n):
            partitionIndex = max(partitionIndex, partition[s[i]])
            if i == partitionIndex:
                result.append(partitionIndex - start + 1)
                start = i + 1
    
        return result