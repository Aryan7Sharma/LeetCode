class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cs,rs,ce,re = s[0], s[1], s[3], s[4]
        return [f"{chr(c)}{r}" for c in range(ord(cs), ord(ce)+1) for r in range(int(rs),int(re)+1)]      