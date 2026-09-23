class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        length = right - left
        width = min(heights[left], heights[right])

        square = length * width

        while left < right:
            length = right - left
            width = min(heights[left], heights[right])
            actual_size = length * width
            square = max(square, actual_size)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        
        return square