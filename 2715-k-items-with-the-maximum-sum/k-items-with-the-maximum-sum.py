class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        maxSum = 0
        while k>0:
            if numOnes>0:
                numOnes-=1
                maxSum+=1
            elif numZeros:numZeros-=1
            else:maxSum-=1
            k-=1
        return maxSum

            