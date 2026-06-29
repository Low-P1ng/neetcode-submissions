class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(i, left):
            if (i,left) in memo:
                return memo[(i,left)]
            if left<0:
                return False
            if i >= len(s):
                return left == 0
            if s[i] == '(':
                memo[(i,left)] = dfs(i+1, left+1)
            if s[i] == ')':
                memo[(i,left)] = dfs(i+1, left-1)
            if s[i] == '*':
                memo[(i,left)] = dfs(i+1, left) or dfs(i+1, left+1) or dfs(i+1, left-1)
            return memo[(i,left)]
        return dfs(0,0)

            
