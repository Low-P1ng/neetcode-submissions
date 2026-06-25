class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = [0]
        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c,val):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                matrix[r][c] <= val):
                return 0
            
            if (r,c) in memo: return memo[(r,c)]

            memo[(r,c)] = max(1+dfs(r+1,c,matrix[r][c]),
                              1+dfs(r-1,c,matrix[r][c]),
                              1+dfs(r,c+1,matrix[r][c]),
                              1+dfs(r,c-1,matrix[r][c]))
            return memo[(r,c)]

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,-1)
        return max(memo.values())