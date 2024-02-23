class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        # loop through the list and create the phrase from the columns and compare it with the sorted of that phrase
        for i in range(len(strs[0])):
            word = ""
            for j in range(len(strs)):
                word += strs[j][i]
            if word != "".join(sorted(word)):
                count += 1
        
        return count
