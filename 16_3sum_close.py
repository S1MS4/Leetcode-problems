class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        mini = nums[0]+nums[1]+nums[2]
        odiff = abs(mini-target)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                diff = abs(total-target)
                if diff < odiff:
                    mini = total
                    odiff = diff 
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return mini
        return mini

print(Solution().threeSumClosest([0,0,0], 10000))