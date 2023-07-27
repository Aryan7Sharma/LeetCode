class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        ans = []
        curr = 0
        for ab in zip(A,B):
            for i in ab:
                if i in seen:curr+=1
                seen.add(i)
            ans.append(curr)
        return ans

            
        
