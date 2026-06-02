class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        # land -> water
        for i in range(len(landStartTime)):
            finish_land = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                ans = min(
                    ans,
                    max(finish_land, waterStartTime[j]) + waterDuration[j]
                )

        # water -> land
        for i in range(len(waterStartTime)):
            finish_water = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                ans = min(
                    ans,
                    max(finish_water, landStartTime[j]) + landDuration[j]
                )

        return ans