class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i, facts = 1,[]
        while i<=n:
            if(n%i==0):facts.append(i)
            i+=1
        return facts[k-1] if k-1<len(facts) else -1