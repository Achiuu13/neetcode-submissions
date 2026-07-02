class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            m = [0] * 26
            for c in s:
                m[(ord(c) - ord('a'))] += 1
            ans[tuple(m)].append(s)
        return list(ans.values())
