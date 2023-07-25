class Solution:
    def sortVowels(self, s: str) -> str:
        vowelsHashmap = {"A":0,"E":0,"I":0,"O":0,"U":0,"a":0,"e":0,"i":0,"o":0,"u":0}
        for i in s:
            if i in vowelsHashmap:vowelsHashmap[i]+=1
        sortedVowels = ""
        for k,v in vowelsHashmap.items():
            for j in range(v):sortedVowels+=k
        sSorted = ""
        vowelIndex = 0
        for i in s:
            if i in vowelsHashmap:
                sSorted+=sortedVowels[vowelIndex]
                vowelIndex+=1
            else:sSorted+=i
        return sSorted