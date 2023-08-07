class Solution:
    def finalString(self, s: str) -> str:
        newS = ""
        for char in s:
            if char=="i":newS=newS[::-1]
            else:newS+=char
        return newS