class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # step 1: sort the array
        nums.sort()
        final = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            a = i
            b = i + 1
            c = len(nums) - 1
            while b < c:
                if nums[b] + nums[c] > - nums[a]:
                    c -= 1
                elif nums[b] + nums[c] < - nums[a]:
                    b += 1
                else:
                    final.append([nums[a], nums[b], nums[c]])
                    b +=1
                    c -=1
                    while b < c and nums[b] == nums[b -1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
        return final