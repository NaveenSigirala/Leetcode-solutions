class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for i in range(len(encoded)):
            s=encoded[i]^l[i]
            l.append(s)
        return l
