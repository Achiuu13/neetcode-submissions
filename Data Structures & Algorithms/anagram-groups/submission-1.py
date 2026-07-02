class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            m = [0] * 26
            for c in s:
                m[ord(c) - ord('a')] += 1
            res[tuple(m)].append(s)
        return list(res.values())
        