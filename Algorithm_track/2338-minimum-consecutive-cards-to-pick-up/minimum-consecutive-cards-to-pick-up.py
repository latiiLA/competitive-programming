class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        result = float('inf')
        i = 0

        dictionary = {}
        
        for j in range(n):
            dictionary[cards[j]] = dictionary.get(cards[j], 0) + 1

            while dictionary[cards[j]] > 1:
                result = min(result, j - i + 1)
                dictionary[cards[i]] -= 1
                if dictionary[cards[i]] == 0:
                    del dictionary[cards[i]]
                i += 1
        
        if result == float('inf'): 
            return -1 
        else:
            return result
