class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmapS,hashmapT = {},{}
        miniSteps = 0
        for i in s:
            if i not in hashmapS:hashmapS[i]=1
            else:hashmapS[i]+=1
        for j in t:
            if j not in hashmapT:hashmapT[j]=1
            else:hashmapT[j]+=1
        #print(hashmapS,hashmapT)
        for k,v in hashmapS.items():
            if k not in hashmapT:miniSteps+=v
            elif v>hashmapT[k]:miniSteps+=v-hashmapT[k]
            else:continue
        #print(miniSteps)
        for k,v in hashmapT.items():
            if k not in hashmapS:miniSteps+=v
            elif v>hashmapS[k]:miniSteps+=v-hashmapS[k]
            else:continue
        return miniSteps

