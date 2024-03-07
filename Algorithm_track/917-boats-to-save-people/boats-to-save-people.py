class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0

        # point the pointers at the beginning and at the end. remove the largest element while counting if they are greater than the limit
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            elif people[left] >= people[right]:
                left += 1
            elif people[right] > people[left]:
                right -= 1

            count += 1

        return count