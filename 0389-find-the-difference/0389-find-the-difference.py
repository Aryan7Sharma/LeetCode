class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap={}
        for j in s:
            if j not in hashmap:
                hashmap[j]=1
            else:
                hashmap[j]+=1
        for i in t:
            if i in hashmap:
                hashmap[i]-=1
                if hashmap[i] == 0:
                    del hashmap[i]
            else:
                return i

            
        