class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans  = [0,0]
        for rowInd in range(len(mat)):
            countOne=0
            for v in mat[rowInd]:
                if v==1:countOne+=1
                else:continue
            if countOne>ans[-1]:ans=[rowInd,countOne]
        return ans
