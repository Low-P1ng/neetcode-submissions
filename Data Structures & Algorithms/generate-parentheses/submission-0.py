class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l,r,cur):
            if l==r==n:
                res.append(cur[:])
                return

            if l<n:  
                dfs(l+1,r,cur+'(')
                if l>r:
                    dfs(l,r+1,cur+')')

            else:
                dfs(l,r+1,cur+')')

        dfs(0,0,'')
        return res

            
            