class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # the pairs needs to be sorted based on their position
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs = sorted(pairs)[::-1]

        # One core point is target - position helps to find the distance then you will get the acceleration
        # do that using monotonic stack the length of that stack will be the solution
        for position, speed in pairs:
            temp = (target - position) / speed
            stack.append(temp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
    
        return len(stack)