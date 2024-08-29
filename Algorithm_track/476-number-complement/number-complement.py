class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        exponent = 0

        while num > 0:
            comp = 1 if num&1 == 0 else 0
            complement += comp  * 2 ** exponent
            exponent += 1            
            num >>= 1

        return complement