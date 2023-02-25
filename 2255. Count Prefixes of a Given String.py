class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for word in words:
            if s.startswith(word):
                c += 1
        return c
