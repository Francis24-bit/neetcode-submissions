class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1

        while left <= right:
            mid_index = left + (right - left) // 2
            row = mid_index // n
            column = mid_index % n
            mid_number = matrix[row][column]

            if mid_number < target:
                left = mid_index + 1
            elif mid_number > target:
                right = mid_index - 1
            else:
                return True
        
        return False