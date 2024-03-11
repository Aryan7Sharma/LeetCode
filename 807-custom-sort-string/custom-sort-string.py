class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sDict = {}
        res = ""
        for i in s:
            if i in sDict:sDict[i]+=1
            else:sDict[i]=1
        for chr in order:
            if chr in sDict:
                res+=chr*sDict[chr]
                del sDict[chr]
        for chr in sDict.keys():
            res+=chr*sDict[chr]
        return res

        