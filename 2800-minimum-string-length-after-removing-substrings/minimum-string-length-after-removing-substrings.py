class Solution:
    def minLength(self, s: str) -> int:
        while len(s)!=0:
            s = s.replace("AB","")
            s = s.replace("CD","")
            if ("AB" not in s) and ("CD" not in s):break
        return len(s)