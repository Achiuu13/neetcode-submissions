class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            comp = target - nums[i]
            if comp in m:
                return [m[comp], i]
            else:
                m[n] = i