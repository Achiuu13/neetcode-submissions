class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]

        bestIndex = 0
        maxLength = 0

        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if length > maxLength:
                        maxLength = length
                        bestIndex = i
        return s[bestIndex:bestIndex + maxLength]
                        