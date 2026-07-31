class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        ro = [0]
        visited = set()
        def addq(r,c):
            if (r<0 or r>= rows or
                c<0 or c>= cols or
                (r,c) in visited or
                grid[r][c] == 0):
                return
            visited.add((r,c))
            q.append((r,c))
            ro[0]-=1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    ro[0]+=1

        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                addq(r+1,c)
                addq(r-1,c)
                addq(r,c+1)
                addq(r,c-1)

            time+=1

        return max(0,time-1) if ro[0] == 0 else -1