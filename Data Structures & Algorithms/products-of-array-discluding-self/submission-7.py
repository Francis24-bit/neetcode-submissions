class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        result = 1
        for i in range (1, len(nums)):
            result = result * nums[i - 1]
            left.append(result)
        
        right = [1]
        result = 1
        for i in range (len(nums)-2 , -1, -1):
            result = result * nums[i + 1]
            right.append(result)
        right.reverse()
    
        final = []
        for i in range(len(nums)):
            final.append(left[i] * right [i])
        return final