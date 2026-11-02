class PrefixTree:

    def __init__(self):
        self.m = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.m:
                curr.m[c] = PrefixTree()
            curr = curr.m[c]
        curr.end = True
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.m:
                return False
            curr = curr.m[c]
        return curr.end
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.m:
                return False
            curr = curr.m[c]
        return True
        