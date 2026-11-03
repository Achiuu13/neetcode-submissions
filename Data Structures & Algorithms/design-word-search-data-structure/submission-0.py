class WordDictionary:

    def __init__(self):
        self.m = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.m:
                curr.m[c] = WordDictionary()
            curr = curr.m[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.end
            c = word[i]
            if c == ".":
                for nei in curr.m.values():
                    if dfs(i + 1, nei): return True
                return False
            if c not in curr.m:
                return False
            else:
                return dfs(i + 1, curr.m[c])
        return dfs(0, self)




