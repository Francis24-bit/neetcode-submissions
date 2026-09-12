class Solution:
    def search(self, nums: List[int], target: int) -> int:
# find mid first
# if nums[mid] == target, return mid
# otherwise, check which half is sorted
# if target is inside the sorted half, keep that half
# if target is outside the sorted half, discard that half
# since mid was already checked, move to mid - 1 or mid + 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] <= nums[right]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1