class Solution:
    def minLength(self, s: str) -> int:
        flag = True
        while flag:
            countOccr = 0
            for i in range(len(s)-1):
                if (s[i] == "A" and s[i+1] == "B") or (s[i] == "C" and s[i+1] == "D"):
                    s=s[:i]+s[i+2:]
                    countOccr+=1
                    break
                else:continue
            if countOccr == 0:flag = False
        return len(s)
