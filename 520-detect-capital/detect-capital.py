class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2: return True
        category = None
        firstword = word[0]
        secondword = word[1]
        if firstword.upper()==firstword and secondword.upper()==secondword: category = 65
        else: category = 97
        for i in word[1:]:
            value = ord(i) -  category
            if value>25 or value<0: return False
        return True
        