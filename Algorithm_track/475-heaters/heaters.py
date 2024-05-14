class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''Binary Search Appraoch, 
        This is different from the bruteforce in finding the closest distance to the house
        '''
        result = 0

        # heaters needs to be sorted
        heaters.sort()
        for house in houses:
            left = 0 # minimum distance we can encounter
            right = len(heaters) - 1 # maximum distance we can encounter
            minimum_distance = float('inf')

            # binary searching for the closest distance
            while left <= right:
                mid = (left + right) // 2
                distance = abs(heaters[mid] - house)
                minimum_distance = min(minimum_distance, distance) # keep track of the minimum distance we can have

                # move our pointers of binary search
                if heaters[mid] >= house:
                    right = mid - 1
                else:
                    left = mid + 1
            
            result = max(result, minimum_distance) # find the maximum distance for all the houses.
        
        return result

        # Overall complexity of this algorithm is O(nlogn) -- because it sorting is involved


        '''

        # Bruteforce Approach
        dictionary = {}

        for house in houses:
            distance = float('inf')
            for heater in heaters:
                distance = min(distance, abs(heater - house))
            
            dictionary[house] = distance

        return max(dictionary.values())

        '''