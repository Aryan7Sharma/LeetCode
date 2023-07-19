class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedLine,length = sorted(heights),len(heights)
        expectNotMatch = 0
        for i in range(length):
            if expectedLine[i]!=heights[i]:expectNotMatch+=1
        return expectNotMatch
