class Solution:
    def romanToInt(self, s: str) -> int:
        lenS = len(s)
        romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        output = 0
        currIndex = 0
        while currIndex<lenS-1:
            currRomanValue = romanDict[s[currIndex]]
            nextRomanValue = romanDict[s[currIndex+1]]
            if(nextRomanValue>currRomanValue):
                output+=nextRomanValue-currRomanValue
                currIndex+=2
            else:
                output+=currRomanValue
                currIndex+=1
        if(romanDict[s[lenS-1]]<=romanDict[s[lenS-2]]):
            output+=romanDict[s[lenS-1]]
        return output