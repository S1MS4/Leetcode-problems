class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(',']':'[','}':'{'}
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack[-1] != dic[char]:
                    return False
                else:
                    stack.pop()
        return not stack
print(Solution().isValid("(]"))