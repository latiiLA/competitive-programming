class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        index = 0
        
        # loop through the array and find the unique character and its count
        while i < len(chars):
            j = i

            # count the cccurance of a given characters
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            
            chars[index] = chars[i]
            index += 1

            count = j - i

            if count > 1:
                # append the count as independent character
                for digit in str(count):
                    chars[index] = digit
                    index += 1
                    
            i = j

        return index