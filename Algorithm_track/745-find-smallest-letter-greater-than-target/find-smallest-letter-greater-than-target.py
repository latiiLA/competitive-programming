class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = float('inf')

        for char in letters:
            if char > target:
                result = min(ord(char), result)
        
        if result == float('inf'):
            return letters[0]
        
        return chr(result)