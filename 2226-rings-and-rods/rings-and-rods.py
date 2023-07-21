class Solution:
    def countPoints(self, rings: str) -> int:
        hashmap = {}
        threeColorRods = 0
        for i in range(0,len(rings),2):
            if rings[i+1] not in hashmap:hashmap[rings[i+1]]=[rings[i]]
            else:
                if rings[i] not in hashmap[rings[i+1]]:hashmap[rings[i+1]].append(rings[i])
                else:continue
        print(hashmap)
        for val in hashmap.values():
            if len(val)==3:threeColorRods+=1
        return threeColorRods