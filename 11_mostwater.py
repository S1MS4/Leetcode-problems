# O(n^2)
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         maxi = 0
#         for i, a in enumerate(height):
#             for j, b in enumerate(height[i+1:], start=i+1):
#                 maxi = (min(height[i],height[j])*(abs(j-i))) if ((min(height[i],height[j])*(abs(j-i))) > maxi and i != j) else maxi
#         return maxi

# O(n)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxi = 0
        l,r = 0, len(height)-1
        while l < r:
            width = r-l
            h = min(height[l],height[r])
            maxi = max(maxi,h*width)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxi
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))