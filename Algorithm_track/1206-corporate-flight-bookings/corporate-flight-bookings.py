class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 2)

        # create a prefix using the specified index and reserved booking number
        for i in range(len(bookings)):
            prefix[bookings[i][0]] += bookings[i][2]
            prefix[bookings[i][1] + 1] -= bookings[i][2]
        
        # print(prefix)

        # create the sum of the prefix to get number of bookings for each flight
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + prefix[i]
        
        return prefix[1:n+1]

