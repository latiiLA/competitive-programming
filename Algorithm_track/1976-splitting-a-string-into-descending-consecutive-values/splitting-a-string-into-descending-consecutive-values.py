class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtracking(i, val):
            if i == len(s): #if this happens that means we have looped through the array and the conditions have been satisfied
                return True

            for j in range(i,  len(s)):
                current = int(s[i:j + 1])
                if current + 1 == val:  # pruning (if this does not satisfy there is no need to further loop through the tree)
                    if backtracking(j + 1, current):
                        return True
            
            return False

        # implement backtracking for every possible combinations. you will have n combinations for each tree branches
        # we will only loop until n - 1 because we need at least two elements to compare
        for i in range(n-1):
            if backtracking(i + 1, int(s[:i + 1])):
                return True

        return False
