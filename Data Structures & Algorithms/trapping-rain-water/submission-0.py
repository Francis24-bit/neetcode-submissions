class Solution:
    def trap(self, height: List[int]) -> int:
        # as the lower bound decides the water level, I need to find the min(maxLeft, maxRight) - height[i]
        # add them accumulatively
        # use 2 arrays to store the leftMax, and rightMax

        if height == []:
            return 0

        leftMax = [0] * len(height)
        leftMax[0] = 0
        for i in range (1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])

        rightMax = [0] * len(height)
        rightMax[-1] = 0
        for i in range (len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height [i + 1])

        water = 0
        for i in range(len(height)):
            water += max(min(leftMax[i], rightMax[i]) - height[i], 0)
        
        return water