class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for i in range(len(landStartTime)):
            combineTime = landStartTime[i]+landDuration[i] 
            for j in range(len(waterStartTime)):
                ans=min(ans, max(combineTime, waterStartTime[j]) + waterDuration[j])
        for i in range(len(waterStartTime)):
            combineTime = waterStartTime[i]+waterDuration[i] 
            for j in range(len(landStartTime)):
                ans=min(ans, max(combineTime, landStartTime[j]) + landDuration[j])
        return ans

        