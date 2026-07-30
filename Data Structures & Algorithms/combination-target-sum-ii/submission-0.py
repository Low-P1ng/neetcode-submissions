class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(candidates) or total > target:
                return

            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue

                path.append(candidates[idx])
                dfs(idx + 1, total + candidates[idx])
                path.pop()

        dfs(0, 0)
        return res