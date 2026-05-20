class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        output = []
        for i in range(len(A)):
            count = 0
            larr = A[:i+1]
            for j in range(0,i+1):
                if B[j] in larr:count+=1
            output.append(count)
        return output
        