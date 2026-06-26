class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s += '-'
            s = s[1:len(s)+1]
        s = s[::-1]
        s = int(s)
        return 0 if s > 2147483648 or s < -2147483648 else s

# print(Solution().reverse(1534236469))