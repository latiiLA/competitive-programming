class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        
        while x > 0 or y > 0:
            if x&1 != y&1: # check if the last bit is the same or not
                count += 1
            # right shift
            x >>= 1
            y >>= 1

        return count

