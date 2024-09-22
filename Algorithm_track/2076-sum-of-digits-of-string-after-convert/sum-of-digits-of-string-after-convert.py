class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = []
        ans = 0

        for char in s:
            result.append(str(ord(char) - 96))

        # print(result)
        while k > 0:
            ans = 0

            for res in result:
                for char in res:
                    ans += int(char)
            
            result = str(ans)
            k -= 1

        return ans