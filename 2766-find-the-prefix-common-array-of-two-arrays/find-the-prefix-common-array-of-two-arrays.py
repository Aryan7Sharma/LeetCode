class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        output=[]
        arrHash = {}
        for i in range(len(A)):arrHash[A[i]]=i

        for i in range(len(B)):
            count = 0
            eIndex = i+1
            for j in range(0,eIndex):
                if B[j] in arrHash and eIndex>arrHash[B[j]]:count+=1
            output.append(count)
        return output
        