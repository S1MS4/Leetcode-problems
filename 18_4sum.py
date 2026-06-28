class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j + 1, len(nums) - 1

                while l < r:
                    curr = nums[i]+nums[j]+nums[l]+nums[r]
                    if curr == target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l +=1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    if curr > target:
                        r -= 1
                    elif curr < target:
                        l += 1
        return result
print(Solution().fourSum([1,0,-1,0,-2,2],0))