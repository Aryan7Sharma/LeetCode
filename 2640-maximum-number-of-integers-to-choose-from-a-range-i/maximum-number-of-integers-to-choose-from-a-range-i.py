class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        maxNum = 0
        sumOfNum = 0
        hashmap = {}
        for i in banned:
            if i not in hashmap:hashmap[i]=1
        for i in range(1,n+1):
            if i not in hashmap and sumOfNum+i<=maxSum:
                maxNum+=1
                sumOfNum+=i
            else:continue 
        return maxNum
