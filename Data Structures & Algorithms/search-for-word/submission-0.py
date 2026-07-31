class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows,Cols = len(board), len(board[0])
        visited = set()
        def dfs(r,c,i):
            if  i == len(word):
                return True
            if (r<0 or r>=Rows or 
                c<0 or c>=Cols or
                board[r][c]!=word[i] or
                (r,c) in visited):
                return False

            visited.add((r,c))
            found = (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            visited.remove((r,c))
            return found
        for i in range(Rows):
            for j in range(Cols):
                if dfs(i,j,0):
                    return True

        return False
        

            