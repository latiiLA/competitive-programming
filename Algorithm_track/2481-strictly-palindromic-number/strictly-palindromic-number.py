class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        for i in range(1, n - 1):

            representation_without_prefix = bin(i)[2:] # finds binary representation of the number

            j = 0
            k = len(representation_without_prefix) - 1

            # checks if the number satisfies the condition between 2 , n - 2
            while j < k:
                if representation_without_prefix[j] != representation_without_prefix[k]:
                    return False
                j += 1
                k -= 1
            
        return True            
        