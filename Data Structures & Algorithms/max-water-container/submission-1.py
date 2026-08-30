class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the area is limited by the min height * the width (2 pointers, starting from the 2 ends of the array)
        # move the smaller height inward to inerate an area every round

        pointer1 = 0
        pointer2 = len(heights) - 1
        max_area = 0

        while pointer1 < pointer2:
            width = pointer2 - pointer1
            height = min(heights[pointer1], heights[pointer2])
            area = width * height
            max_area = max(max_area, area)

            if height == heights[pointer1]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return max_area