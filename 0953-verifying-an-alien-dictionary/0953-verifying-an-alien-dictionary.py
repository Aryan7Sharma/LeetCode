class Solution:
    def isAlienSorted(self, w: List[str], order: str) -> bool:
        hashmap={}
        for i,val in enumerate(order):
            hashmap[val]=i
        for i in range(len(w)-1):
            for j in range(len(w[i])):
                if j>=len(w[i+1]):return False
                if w[i][j]!=w[i+1][j]:
                    if hashmap[w[i][j]]>hashmap[w[i+1][j]]:return False
                    break
        return True