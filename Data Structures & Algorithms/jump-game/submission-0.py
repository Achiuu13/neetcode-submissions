class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currMax = 0

        for i, num in enumerate(nums):
            if i > currMax:
                return False
            currMax = max(currMax, i + num)
        return True