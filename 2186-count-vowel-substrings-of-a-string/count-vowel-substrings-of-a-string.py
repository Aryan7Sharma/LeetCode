class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        i = 0
        length = len(word)
        subsetLen = 5
        countVowelSubstrings = 0
        while i<length-4:
            currSubSet = set(list(word[i:i+subsetLen]))
            if currSubSet.issubset(vowels) and subsetLen<=length-i:
                if len(currSubSet)==5:countVowelSubstrings+=1
                subsetLen+=1
            else:
                subsetLen = 5
                i+=1
        return countVowelSubstrings



