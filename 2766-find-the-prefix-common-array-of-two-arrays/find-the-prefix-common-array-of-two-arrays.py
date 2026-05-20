class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        output=[]
        hashmap = {A[0]:1}
        if B[0] in hashmap:
            hashmap[B[0]]+=1
            output.append(1)
        else:
            hashmap[B[0]]=1
            output.append(0)

        for i in range(1,len(A)):
            prev = output[-1]
            numA = A[i]
            numB = B[i]
            if numA in hashmap:
                hashmap[numA]=1
                prev+=1
            else:hashmap[numA]=1
            if numB in hashmap:
                hashmap[numB]=1
                prev+=1
            else:hashmap[numB]=1
            output.append(prev)
        return output
        