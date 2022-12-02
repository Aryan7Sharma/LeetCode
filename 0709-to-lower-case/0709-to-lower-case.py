class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in s:
            if ord(i)>64 and ord(i)<91:
                ans+=i.lower()
            else:
                ans+=i
        return ans
                