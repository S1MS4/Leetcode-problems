class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        curr = 0
        going_down = False
        for char in s:
            rows[curr] += char
            if curr == 0 or curr == numRows-1:
                going_down = not going_down
            curr += 1 if going_down else -1
        return ''.join(rows)
#example usage:
print(Solution().convert("PAYPALISHIRING", 3))  # Output: ['PAHN', 'APLSIIG', 'YIR']