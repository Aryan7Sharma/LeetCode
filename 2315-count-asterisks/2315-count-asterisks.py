class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = None
        countAsk = 0
        for i in s:
            if i == "*":
                if not pair:
                    countAsk+=1
            elif i == "|":
                if pair:
                    pair = None
                else:
                    pair = 1
        return countAsk
        