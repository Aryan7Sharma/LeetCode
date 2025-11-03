class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        output = []
        outputhash = {}
        outputhash[s[0:10]]=1
        slen = len(s)        
        for i in range(1,slen-9):
            comb = s[i:i+10]
            if comb in outputhash:outputhash[comb]+=1
            else:outputhash[comb]=1
        for k,v in outputhash.items():
            if v>1:output.append(k)
        return output

        