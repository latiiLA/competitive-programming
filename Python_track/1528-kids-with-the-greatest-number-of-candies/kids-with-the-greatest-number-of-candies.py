class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        greatest_number_of_candies = []
        maximum_candy = max(candies)

        # Finding greatest number of candies after adding extracandies
        for candy in candies:
            if candy + extraCandies >= maximum_candy:
                greatest_number_of_candies.append(True)
            else:
                greatest_number_of_candies.append(False)  

        return greatest_number_of_candies        