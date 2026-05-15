class Solution:
    def findMin(self, nums: List[int]) -> int:
        miniele = float(inf)
        for i in nums:
            if i<miniele:miniele=i
        return miniele
        