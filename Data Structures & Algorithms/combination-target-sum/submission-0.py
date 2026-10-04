class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        start = 0
        combo = []
        total = 0
        def helper(start, combo, total):
            if total == target:
                res.append(combo.copy())     
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                combo.append(nums[i])
                total += nums[i]
                helper(i, combo, total)
                total -= nums[i]
                combo.pop()
        helper(start, combo, total)
        return res