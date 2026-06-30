class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def recurse(s: str, opens: int, closed: int):
            if len(s) == n*2:
                res.append(s)
                return
            
            if opens < n:
                recurse(s+"(",opens+1,closed)
            if closed < opens:
                recurse(s+")",opens,closed+1)
            
        recurse("",0,0)
        return res
    
print(Solution().generateParenthesis(3))