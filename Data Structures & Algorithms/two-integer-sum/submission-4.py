class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need = target - nums[i]

        for i in range (len(nums)):
            need = target - nums[i]
            if need in nums [i+1:]:
                j = nums.index(need, i + 1)
                if j!= i:
                    return [i, j]