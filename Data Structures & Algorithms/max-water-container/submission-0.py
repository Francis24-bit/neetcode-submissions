class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #start with the 2 ends of the array, get the area

        pointer1 = 0
        pointer2 = len(heights) - 1
        max_area = 0

        while pointer1 < pointer2:
            width = pointer2 - pointer1
            height = min(heights[pointer1], heights[pointer2])
            area = width * height

            if height == heights[pointer1]:
                pointer1 += 1
            else:
                pointer2 -= 1

            max_area = max(max_area, area)
        
        return max_area
            
            
