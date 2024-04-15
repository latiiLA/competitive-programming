class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        result = 0
        i = 0
        j = len(piles) - 1

        # Give the maximum to Alice, take the next maximum for yourself, give the minimum element of the array to Bob
        while i <= j:
            j -= 1
            result += piles[j]
            j -= 1
            i += 1
    
        return result