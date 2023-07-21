class Solution:
    def checkString(self, s: str) -> bool:
        aInd = -1
        bInd = 101
        for i in range(len(s)):
            if s[i]=="a":aInd = i
            else:bInd = min(bInd,i)
        return True if aInd==-1 or aInd==101 else bInd>aInd