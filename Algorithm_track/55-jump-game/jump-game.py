class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        First Approach
        Loop through the nums and jump your pointer by the amount of the value at that pointer
        If the value if zero break the loop because it creates infinitive loop
        If pos becomes greater or equal to n - 1 that means it has reached the end...return True else False

        The correct approach
        if current jump is less than the next jump...take one jump and take the next jump
        else take the previous jump...
        '''    
        jumps = 0

        # [1,1]

        for i in range(len(nums)):
            if jumps < nums[i]:
                jumps = nums[i]

            if not jumps: break
            jumps -= 1

        return True if i == len(nums) -1 else False
