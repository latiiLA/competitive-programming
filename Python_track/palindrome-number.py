class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # result = 0
        # temp = x

        # while x > 0:
        #     result = result * 10 + x % 10
        #     x = x // 10

        # print(result)

        # return result == temp

        num_string = str(x)

        return num_string == num_string[::-1]

