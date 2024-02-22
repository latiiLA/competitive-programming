class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        
        game = list(range(n))
        
        ptr = 0
        
        while len(game) > 1:
           ptr = (ptr + k - 1) % len(game)
           game.pop(ptr)
        
        return game[0] + 1