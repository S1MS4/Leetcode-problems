# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         min_len = min(len(s) for s in strs)
#         for i in range(min_len):
#             char = strs[0][i]
#             for string in strs:
#                 if any(s[i]!=char for s in strs):
#                     return strs[0][:i]
#         return strs[0][:min_len]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        return first[:i]
    
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
