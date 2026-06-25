class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,temp):
            if (i,temp) in memo:
                return memo[(i,temp)]
            if temp == t:
                return 1
            if i >= len(s) or len(temp) > len(t):
                return 0

            memo[(i,temp)] = dfs(i+1,temp+s[i]) + dfs(i+1,temp)
            return memo[(i,temp)]
            
        return dfs(0,'')
