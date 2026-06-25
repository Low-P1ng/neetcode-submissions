class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if len(s) - i < len(t) - j: return 0
            
            if j == len(t):
                return 1

            if i >= len(s):
                return 0

            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i,j)]

        return dfs(0,0)
