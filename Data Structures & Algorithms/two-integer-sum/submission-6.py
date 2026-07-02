class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in m:
                return [m[comp], i]
            m[num] = i
        return []