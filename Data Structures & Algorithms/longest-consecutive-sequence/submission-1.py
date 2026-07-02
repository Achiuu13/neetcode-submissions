class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        s = set()

        longest = 1
        curr = 1

        for num in nums:
            s.add(num)

        for n in s:
            if n - 1 not in s:
                i = 1
                while n + i in s:
                    curr += 1
                    i += 1
                longest = max(curr,longest)
                curr = 1
        return longest


