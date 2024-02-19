class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        watering_capacity = capacity

        # Find number of steps--add 1 if capacity is greater than plants[i] else add refill and watering costs
        for i in range(len(plants)):
            if plants[i] <= capacity:
                steps += 1
                capacity -= plants[i]
            else:
                capacity = watering_capacity
                steps += i * 2 + 1
                capacity -= plants[i]
        return steps