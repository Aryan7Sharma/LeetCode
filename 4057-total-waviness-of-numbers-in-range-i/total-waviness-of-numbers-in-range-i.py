class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for i in range(num1,num2+1):
            if i<99:continue
            numChar = str(i)
            s,e=0,len(numChar)-1
            while e-s>1:
                firstNum = int(numChar[s])
                middleNum = int(numChar[s+1])
                lastNum = int(numChar[s+2])
                if middleNum>firstNum and middleNum>lastNum:ans+=1
                elif middleNum<firstNum and middleNum<lastNum:ans+=1
                s+=1
        return ans

        