class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
    

        number = list(int(num) for num in nums)
        number.sort(reverse=1)

        return str(number[k-1])
