class Solution:
    def smallestNumber(self, num: int) -> int:

        numValue = num

        if num < 0:
            num = num * -1

        num = list(str(num))
        num.sort()

        if numValue > 0:
            i = 0
            flag2 = False

            while num[i] == '0' and i < len(num) - 1:
                i += 1
                flag2 = True

            if flag2:
                num[0], num[i] = num[i], num[0]
                          
            num = "".join(num)

            num = int(num)

            return num
        
        elif numValue < 0:
            num.reverse()
            i = 0
            flag2 = False

            while num[i] == '0' and i < len(num) - 1:
                i += 1
                flag2 = True

            if flag2:
                num[0], num[i] = num[i], num[0]
                
            num = "".join(num)

            num = int(num)

            num = num * -1

            return num

        else:
            return 0