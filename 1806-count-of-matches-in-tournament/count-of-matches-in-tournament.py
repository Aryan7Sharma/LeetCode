class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalMatches = 0
        while n>1:
            totalMatches+=n//2
            if n%2!=0:n = n//2+1
            else: n = n//2
        return totalMatches
