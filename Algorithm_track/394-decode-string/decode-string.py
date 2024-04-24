class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        # loop through the string and add elements until you find closing bracket. when you do pop and do some calculation
        for char in s:
            if char is not ']':
                stack.append(char)
            else:
                # acquire the word
                word = deque()
                while stack[-1] is not '[':
                    word.appendleft(stack.pop())
                stack.pop()

                # acquire the number the word is multiplied by
                number = deque()
                while stack and stack[-1].isdigit():
                    number.appendleft(stack.pop())
                
                stack.append("".join(word) * int("".join(number)))

        return "".join(stack)
