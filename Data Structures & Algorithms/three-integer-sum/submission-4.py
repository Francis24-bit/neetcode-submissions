class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the number so that you can use the 2 pointer mechanism(target too small, move the left pointer, and too big, move the right pointer)
        # use a new list, and list can not append 3 elemetns at the same time, you need to add a list.

        # attention: for duplicates: if the number[k]== numbers [k -1], skip. and it holds true for the other 2 pointers. but as k is the in the for loop, so use if, and we manually increment the other 2 pointers, use while. 

        nums.sort()
        result = []

        for k in range(0, len(nums)):
            left = k + 1
            right = len(nums) - 1

            #to remove duplicates: if the next = before, skip
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while left < right:
                if nums[left] + nums[right] < - nums[k]:
                    left += 1
                elif nums[left] + nums[right] > - nums[k]:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], nums[k]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result