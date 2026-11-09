class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(used, combo):
            if len(combo) == len(nums):
                res.append(combo.copy())
                return
            for num in nums:
                if num not in used:
                    combo.append(num)
                    used.add(num)
                    helper(used, combo)
                    used.remove(num)
                    combo.pop()
        helper(set(), [])
        return res