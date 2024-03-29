class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        i = 0
        j = 0

        n = len(fruits)
        result = 0

        fruits_dict = defaultdict(int)

        # update dictionary. if the length becomes greater than 2 slide the window
        while j < n:
            fruits_dict[fruits[j]] += 1

            while len(fruits_dict) > 2:
                fruits_dict[fruits[i]] -= 1
                if fruits_dict[fruits[i]] == 0:
                    del fruits_dict[fruits[i]]
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result



