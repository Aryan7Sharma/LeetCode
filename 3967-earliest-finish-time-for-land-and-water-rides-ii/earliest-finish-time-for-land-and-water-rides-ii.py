class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def ride_min_time(s1, d1, s2, d2):
            finish1 = float('inf')
            for i in range(len(s1)):
                finish1 = min(finish1, s1[i]+d1[i])
            finish2 = float('inf')
            for i in range(len(s2)):
                finish2 = min(finish2, max(finish1, s2[i])+d2[i])
            return finish2
        startWithLandRide = ride_min_time(landStartTime,landDuration,waterStartTime,waterDuration)
        startWithWaterRide = ride_min_time(waterStartTime,waterDuration,landStartTime,landDuration)

        
        return min(startWithLandRide,startWithWaterRide)


        