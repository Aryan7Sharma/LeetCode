class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        maxPairs = 0
        for i in range(len(words)):
            currRevWord = words[i][::-1]
            for j in range(i+1,len(words)):
                if currRevWord == words[j]:maxPairs+=1
        return maxPairs