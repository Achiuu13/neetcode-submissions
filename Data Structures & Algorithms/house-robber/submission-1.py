class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        opt = [0] * len(nums)
        opt[0] = nums[0]
        opt[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            opt[i] = max(opt[i-1], nums[i] + opt[i-2])
        return opt[len(nums) - 1]
            