class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0

        # approach 2: using bit masking
        for i in range(32):
            total = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32 - 1)
                total += (num >> i) & 1

            total %= 3
            single |= total << i


        if single >= 2**31:
            single -= 2**32

        return single