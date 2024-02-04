class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_value = 0

        # finds the result of the operations
        for operation in operations:
            if operation == "--X" or operation == "X--":
                final_value -= 1
            elif operation == "++X" or operation == "X++":
                final_value += 1
        
        return final_value
