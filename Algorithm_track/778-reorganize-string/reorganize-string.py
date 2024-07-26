class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)
        # print(freq)

        heap = []
        result = []

        for letter, value in freq.items():
            heappush(heap, (-value, letter))

        # print(heap)

        while heap:
            current = []

            for i in range(2):
                if heap:
                    value, letter = heappop(heap)
                    result.append(letter)
                    if value != -1:
                        value += 1
                        current.append((value, letter))
                elif current:
                    return ""
            

            while current:
                heappush(heap, current.pop())

            # print(result, current)
                
            
        return "".join(result)

        