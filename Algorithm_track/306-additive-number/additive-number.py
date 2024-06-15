class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        def backtracking(i, res):
            if i == n:
                return len(res) >= 3
            
            curr = 0
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                curr = curr * 10 + ord(num[j]) - ord('0')
                if len(res) < 2 or curr == res[-2] + res[-1]:
                    res.append(curr)
                    if backtracking(j + 1, res):
                        return True
                    res.pop()
            
            return False

        return backtracking(0, [])