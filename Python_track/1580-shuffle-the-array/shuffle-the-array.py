class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        shuffled = []
        # Shuffling the array
        i = 0
        j = i + n
        while(i<n):
            shuffled.append(nums[i])
            shuffled.append(nums[j])
            i += 1
            j += 1
        
        return shuffled