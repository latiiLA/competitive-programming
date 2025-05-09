# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        minOperations = []

        for i in range(len(boxes)):
            num_operation = 0

            for j in range(len(boxes)):
                if i == j:
                    continue
                elif boxes[j] == "1":
                    num_operation += abs(i - j)
            
            minOperations.append(num_operation)
                
        return minOperations