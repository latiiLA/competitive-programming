class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            
            while i > 0:
                if i & 1 == 1: # and it with 1 then right shift
                    count += 1
                i >>= 1
            result.append(count)

        return result