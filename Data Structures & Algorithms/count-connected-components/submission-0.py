class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        maped = {i:[] for i in range(n)}
        visited = set()
        res = 0
        for n1,n2 in edges:
            maped[n1].append(n2)
            maped[n2].append(n1)

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for child in maped[node]:
                dfs(child)
            return True

        for i in range(n):
            if not dfs(i):
                continue
            res+=1

        return res