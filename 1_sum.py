class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapper = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mapper:
                return [mapper[complement], i]
            mapper[num] = i
        