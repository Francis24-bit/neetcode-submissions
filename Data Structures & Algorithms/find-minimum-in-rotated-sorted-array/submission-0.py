class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find left, mid, right. compare mid and right
        # if mid < right, you can eliminate (mid + 1， right), and right = mid
        # if mid > right, means the min is between (mid + 1, right). so change left = mid + 1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left] 