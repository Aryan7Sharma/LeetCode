class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        pointshashmap = {}
        countIntegers = 0
        for [start,end] in nums:
            for j in range(start,end+1):
                if j in pointshashmap:continue
                else:
                    pointshashmap[j]=1
                    countIntegers+=1
        return countIntegers
