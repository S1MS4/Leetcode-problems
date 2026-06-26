class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n and s[i] == " ":
            i += 1
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        num = 0
        while i < n and s[i].isdigit():
            num = num*10+int(s[i]) 
            i += 1

        num *= sign
        
        # 4. Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(num, INT_MAX))