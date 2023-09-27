class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        countOnes = s.count('1')
        countZeros = n - countOnes
        return "1" * (countOnes-1) + ("0" * countZeros) + "1"
        