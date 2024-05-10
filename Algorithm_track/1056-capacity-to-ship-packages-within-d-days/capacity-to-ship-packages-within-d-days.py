class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = -1
        right = 0
        # Intiution
        # Calculate the minimum weight that needs to be shipped is maximum of the elements and the maximum is the sum the weights
        for weight in weights:
            left = max(left, weight)
            right += weight

        # Use binary search to do calculate the mid of the weight and calculate the number of days with it
        # If the number of days less increase the left so the mid get increased else decrease the right so the mid get decreased
        while left <= right:
            mid = (left + right) // 2
            numberOfDays = 1
            currWeight = 0

            # Calculate the number of days for each days
            for weight in weights:
                if currWeight + weight > mid:
                    numberOfDays += 1
                    currWeight = 0
                currWeight += weight
            
            if numberOfDays > days:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
