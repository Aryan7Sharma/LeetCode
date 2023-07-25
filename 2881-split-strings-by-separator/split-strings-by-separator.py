class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for i in words:
            currStrSplit = i.split(separator)
            for i in currStrSplit:
                if i!='':output.append(i)
            #print(currStrSplit)
            #output.extend(currStrSplit)
        return output