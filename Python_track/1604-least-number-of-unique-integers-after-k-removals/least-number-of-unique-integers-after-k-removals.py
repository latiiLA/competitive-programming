class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts = Counter(arr)
        # print(count)

        counts = dict(sorted(counts.items(), key=lambda item: item[1]))
        # print(count)

        for count in counts.copy():
            if k == 0:
                return len(counts)
            if counts[count] <= k:
                k = k - counts[count]
                counts.pop(count)
                
            else:
                k = 0
        
        if k == 0:
            return len(counts)