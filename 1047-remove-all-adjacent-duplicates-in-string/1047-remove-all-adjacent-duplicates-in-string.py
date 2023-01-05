class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = [s[0]]
        for i in range(1,len(s)):
            if res and s[i] == res[-1]:
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)
                