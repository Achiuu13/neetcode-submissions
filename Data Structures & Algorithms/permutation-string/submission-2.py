class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1m = {}
        for c in s1:
            s1m[c] = 1 + s1m.get(c, 0)

        for l in range(len(s2)):
            s2m = {}
            for r in range(l, min(len(s2), l + len(s1))):
                s2m[s2[r]] = 1 + s2m.get(s2[r], 0)
            if s2m == s1m:
                return True
            del s2m[s2[l]]
        return False
        
        

            