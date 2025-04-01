class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        sDict = {}
        count = 0 
        for i in s:
            if i in sDict:sDict[i]=[sDict[i][0],count]
            else:sDict[i]=[count,count]
            count+=1
        currMax = 0
        output = []
        for char,sIndexs in sDict.items():
            if sIndexs[0]>currMax:
                output.append(currMax)
                currMax = sIndexs[1]
            else:currMax=max(currMax, sIndexs[1])
        output.append(currMax)
        sSum = 0
        for i in range(1,len(output)):
            sSum+=output[i-1] 
            output[i]=output[i]-sSum
        output[0]=output[0]+1
        return output


