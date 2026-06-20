class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        res = []
        for i in range(0,len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minl = min(len(w1), len(w2))
            if w1[:minl] == w2[:minl] and len(w1) > len(w2):
                return ''
            for j in range(minl):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for elem in adj[c]:
                if dfs(elem): return True
            res.append(c)
            visit[c] = False
            

        for c in adj:
            if dfs(c): return ''

        return ''.join(res)[::-1]

        
