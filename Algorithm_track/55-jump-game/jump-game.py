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
        pos = 0
        count = 0
        n = len(nums)
        if n == 1:
            return True
        while pos < n:
            if count and count < nums[pos]:
                count = nums[pos]
            
            elif count and count > nums[pos]:
                count -= 1
            elif not count and nums[pos] == 0:
                return False
            else:
                count = nums[pos]

            if count == 0 and pos < n - 1:
                return False
            # print(count)
            pos += 1

        return True
