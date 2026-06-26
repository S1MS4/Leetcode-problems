# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         if min(nums) == max(nums) and min(nums) == 0:
#             return [[0, 0, 0]]
#         result = set()
#         for i in range(len(nums)-2):
#             mapper = {}
#             for j in range(i+1, len(nums)):
#                 complement = -nums[i] - nums[j]
#                 if complement in mapper:
#                     result.add(tuple(sorted([nums[i],nums[j],complement])))
#                 mapper[nums[j]] = j
#         return [list(t) for t in result]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue

            l,r = i+ 1, len(nums)-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result

print(Solution().threeSum([-1,0,1,2,-1,-4]))
