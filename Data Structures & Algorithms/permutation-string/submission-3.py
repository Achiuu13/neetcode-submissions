class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Map = {}
        windowMap = {}

        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)
        l = 0
        for r in range(0, len(s2)):
            windowMap[s2[r]] = 1 + windowMap.get(s2[r], 0)
            windowSize = r - l + 1
            if windowSize > len(s1):
                windowMap[s2[l]] -= 1
                if windowMap[s2[l]] == 0:
                    del windowMap[s2[l]]
                l += 1
                windowSize = r - l + 1
            if windowSize == len(s1) and s1Map == windowMap:
                return True
        return False
                
        
        