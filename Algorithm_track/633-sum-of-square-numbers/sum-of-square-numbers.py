class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = floor(sqrt(c))

        # tow pointers to track the squared sums and change the pointers based on the result
        while i <= j:
            temp = i ** 2 + j ** 2
            if temp > c:
                j -= 1
            elif temp < c:
                i += 1
            else:
                return True
            
        return False