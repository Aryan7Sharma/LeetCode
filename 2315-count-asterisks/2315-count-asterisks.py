class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = None
        countE = 0
        for i in s:
            if i == "*":
                if not pair:
                    countE+=1
            elif i == "|":
                if pair:
                    pair = None
                else:
                    pair = 1
        return countE
        