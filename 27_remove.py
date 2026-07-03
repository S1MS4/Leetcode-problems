class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i, v in enumerate(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
