class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        

        def grammar(row, k):
            if row == 1:
                return 0
            
            total = 2 ** (row - 1)
            half = total // 2

            if k > half:
                return 1 - grammar(row, k - half)

            return grammar(row - 1, k)

        return grammar(n, k)