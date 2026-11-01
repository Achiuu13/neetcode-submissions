class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = [0] * len(nums)
        minDp = [0] * len(nums)

        maxDp[0] = minDp[0] = nums[0]

        for i in range(1, len(nums)):
            maxDp[i] = max(maxDp[i - 1] * nums[i], minDp[i - 1] * nums[i], nums[i])
            minDp[i] = min(maxDp[i - 1] * nums[i], minDp[i - 1] * nums[i], nums[i])           
        return max(maxDp)