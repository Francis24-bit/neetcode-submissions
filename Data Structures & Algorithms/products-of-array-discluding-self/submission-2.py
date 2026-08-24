class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        result = 1
        for i in range(1, len(nums)):
            left.append(result * nums[i-1])
            result = result * nums[i-1]
        
        right = []
        right.append(1)
        result2 = 1
        for i in range(len(nums) - 2, -1, -1):
            right.append(result2 * nums[i + 1])
            result2 = result2 * nums[i + 1]
        right.reverse()

        final = []
        for i in range (len(nums)):
            final.append(left[i] * right[i])
        
        return final