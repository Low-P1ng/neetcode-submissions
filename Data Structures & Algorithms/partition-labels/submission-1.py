class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = defaultdict(list)
        res = []
        for i,l in enumerate(s):
            idx[l].append(i)
        startidx = 0
        endidx = idx[s[0]][-1]
        for l in idx.keys():
            if idx[l][0] > endidx:
                res.append(endidx - startidx + 1)
                startidx = idx[l][0]
                endidx = idx[l][-1]
                continue
            endidx = max(endidx, idx[l][-1])
        res.append(endidx - startidx + 1)
        return res
