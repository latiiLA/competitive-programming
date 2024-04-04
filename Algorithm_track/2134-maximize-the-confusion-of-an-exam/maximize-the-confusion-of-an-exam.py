class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        count = k
        counter = k
        result_true= 0
        result_false = 0
        result = 0

        j = 0
        l = 0

        # checking for T and F and maximize their result.
        for i in range(n):
            if answerKey[i] != 'T':
                count -= 1
            else:
                counter -= 1
            
            while j < n and count < 0:
                if answerKey[j] != 'T':
                    count += 1
                j += 1
        
            
            while l < n and counter < 0:
                if answerKey[l] != 'F':
                    counter += 1
                l += 1
            
            result_true = max(result_true, i - j + 1)
            result_false = max(result_false, i - l + 1)
 
        
        return max(result_true, result_false)

