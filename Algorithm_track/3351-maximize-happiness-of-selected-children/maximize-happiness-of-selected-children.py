class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        c = 0
        i = 0
        result = 0
        
        # Loop through the elements and try to calculate the result. 
        # increament how many element you are going to decrement from the elements
        # reverse sorting or sorting the elements and taking the greater element makes the solution to be maximum
        while i < len(happiness) and k > 0:
            if happiness[i] - c > 0:
                result += happiness[i] - c
            else:
                break
            i += 1
            c += 1
            k -= 1
        
        return result