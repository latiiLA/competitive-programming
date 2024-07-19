class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        Calculate the total difference if it becomes 0 or greater than 0 ... we would achieve the circle
        After than find the first index where you got the first positive number
        ...you can change when you got negative number--predict the index ahead
        '''
        current_total = 0
        circuit_total = 0
        start_index = 0

        for i in range(len(gas)):
            current_total += gas[i] - cost[i]
            circuit_total += gas[i] - cost[i]

            if current_total < 0:
                current_total = 0
                start_index = i + 1

        return start_index if circuit_total >= 0 else -1
