class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []
        n = len(A)
        for i in range(n):
            aSubArray = A[:i+1]
            bSubArray = B[:i+1]
            count=0
            for j in aSubArray:
                if j in bSubArray:count+=1
                else:continue
            c.append(count)
        return c

