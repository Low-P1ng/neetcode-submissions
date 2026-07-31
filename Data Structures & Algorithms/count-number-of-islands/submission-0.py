class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        rows, cols = len(grid),len(grid[0])

        def dfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    d = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr,dc in d:
                        if (0 <= (r+dr) < rows and 
                            0 <= (c+dc) < cols and
                            grid[r+dr][c+dc] == '1' and
                            (r+dr,c+dc) not in visited):
                            q.append((r+dr,c+dc))
                            visited.add((r+dr,c+dc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    res+=1

        return res