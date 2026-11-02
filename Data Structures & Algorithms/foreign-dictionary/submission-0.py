class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        m = {}

        for word in words:
            for c in word:
                m[c] = []
        
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    m[w1[j]].append(w2[j])
                    break

        visited = set()
        completed = set()
        res = []

        def dfs(c):
            if c in visited: return False
            if c in completed: return True
            visited.add(c)
            for nei in m[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            completed.add(c)
            res.append(c)
            return True
        
        for c in m:
            if not dfs(c):
                return ""
        return "".join(res[::-1])
                
        
            




