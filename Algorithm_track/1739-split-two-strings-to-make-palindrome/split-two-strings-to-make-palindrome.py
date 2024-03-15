class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        i = 0
        n = len(a)


        while i <= n/2 and a[i] == b[n-1-i]:
            i += 1
        
        j = 0
        while j <= n/2 and b[j] == a[n-1-j]:
            j += 1

        anchor = max(i, j)

        left = anchor
        right = n-1-anchor

        while right - left >= 1 and a[left] == a[right]:
            left += 1
            right -= 1

        if right - left < 1:
            return True


        left = anchor
        right = n-1-anchor

        while right - left >= 1 and b[left] == b[right]:
            left += 1
            right -= 1

        if right - left < 1:
            return True



























    # def checkPalindrome(self, word, l): 
    #     k = 0
    #     l -= 1
    #     while k < l and word[k] == word[l]:
    #         k += 1
    #         l -= 1

    #     if k >= l:
    #         return True

    #     return k >= l

    #     # return checkPalindrome(word[k, l + 1]) or checkPalindrome(word)

    # def checkPalindromeFormation(self, a: str, b: str) -> bool:

    #     n = len(a)

    #     # w = ""
    #     # x = a
    #     # y = ""
    #     # z = b

    #     for i in range(0, n):
    #         if a[i] != b[n - 1 - i]:

    #             # word = w + z
    #             # word2 = y + x
    #             word = a[:i] + b[i:]
    #             word2 = b[:i] + a[i:]

    #             # print(word, word2)

                

    #             result =  self.checkPalindrome(word, n) or self.checkPalindrome(word2, n)

    #             if result:
    #                 return True

    #             # if i < n:
    #             #     w += a[i]
    #             #     z = b[i + 1:]

    #             #     y += b[i]
    #             #     x = a[i + 1:]
            
    #     return False
