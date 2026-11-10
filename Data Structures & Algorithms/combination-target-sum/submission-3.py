class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(start, combo, total):
            if total == target:
                res.append(combo.copy())     
                return
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                combo.append(nums[i])
                helper(i, combo, total + nums[i])
                combo.pop()
        helper(0, [], 0)
        return res