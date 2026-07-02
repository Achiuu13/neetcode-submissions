class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums [i] == nums[i -1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r - 1 and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                    while r > l + 1 and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        return res