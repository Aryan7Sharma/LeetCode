class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(s)
        hashmap = {}
        for i in s:
            if i in hashmap:hashmap[i]+=1
            else:hashmap[i]=1
        #print(hashmap)
        newStr = []
        while hashmap:
            print(hashmap)
            keys = list(hashmap.keys()) # Create a copy of the dictionary keys
            revStr = ""

            #print(newStr)
            for k in keys:
                #print(hashmap,"ch")
                if hashmap[k]>1:
                    revStr+=k
                    hashmap[k]-=2 
                    if hashmap[k]==0:del hashmap[k]
                elif hashmap[k]<=1:del hashmap[k]
            newStr+=keys
            newStr+=revStr[::-1]
        return "".join(newStr)
        

            


                