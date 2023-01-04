class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        for i in s1.split(" "):
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i in s2.split(" "):
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        res = []
        for k,v in hashmap.items():
            if v == 1:
                res.append(k)
        return res
        