class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        
        total = sum(chalk)

        k = k % total

        if n == 1:
            return 0

        # subtract until the k is less than total sum 
        while k >= total:
            k -= total

        # loop through the array and subtract if k is greater than arrays element, otherwise return
        for i in range(n):
            if k >= chalk[i]:
                k -= chalk[i]
            else:
                break

        return i