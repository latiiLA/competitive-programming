class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = 0


        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(n):
            if i == 0:
                leftMax[0] = height[0]
                rightMax[n - 1] = height[n - 1]
            
            else:
                leftMax[i] = max(height[i], leftMax[i- 1])
                rightMax[n - i - 1] = max(height[n- i -1], rightMax[n - i])

        
        for i in range(n):
            trappedWater += min(leftMax[i], rightMax[i]) - height[i]
        
        return trappedWater
