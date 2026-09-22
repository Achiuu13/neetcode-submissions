class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            m[s[r]] = 1 + m.get(s[r], 0)
            maxFreq = max(m.values())
            windowLength = r - l + 1
            while windowLength - maxFreq > k:
                m[s[l]] -= 1
                l += 1
                windowLength = r - l + 1
                maxFreq = max(m.values())
            longest = max(longest, windowLength)
        return longest



