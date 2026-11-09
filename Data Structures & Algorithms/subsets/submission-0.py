class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(index, combo):
            if index == len(nums):
                res.append(combo.copy())
                return
            combo.append(nums[index])
            helper(index + 1, combo)
            combo.pop()
            helper(index + 1, combo)
        helper(0, [])
        return res