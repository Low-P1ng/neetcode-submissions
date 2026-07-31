class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        p = []
        def dfs(start):
            if start >= len(s):
                res.append(p.copy())
                return
            for end in range(start,len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:
                    p.append(s[start:end+1])
                    dfs(end+1)
                    p.pop()

        dfs(0)
        return res
            

