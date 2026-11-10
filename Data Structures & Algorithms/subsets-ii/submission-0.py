class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(index, combo):
            res.append(combo.copy())
            for i in range(index, len(nums)):
                if index < i and nums[i] == nums[i - 1]:
                    continue
                combo.append(nums[i])
                helper(i + 1, combo)
                combo.pop()
        helper(0, [])
        return res