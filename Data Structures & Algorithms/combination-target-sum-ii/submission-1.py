class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()

        def helper(start, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            for i in range(start, len(candidates)):
                if total > target:
                    return
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                helper(i + 1, combo, total + candidates[i])
                combo.pop()
        helper(0, [], 0)
        return res
