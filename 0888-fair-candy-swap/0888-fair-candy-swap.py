class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        setB = set(bobSizes)
        
        for x in aliceSizes:
            if (x + (sumB-sumA)//2) in setB:
                return [x, x+(sumB-sumA)//2]