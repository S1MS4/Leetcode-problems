class Solution:
    def strStr(self, haystack: str, needle: str) -> bool:
        return haystack.find(needle) if needle else -1
        
print(Solution().strStr("hello", "ll"))