class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        char = {'A':1,'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        if len(columnTitle)<2:
            return char[columnTitle[0]]
        coluNum = char[columnTitle[-1]]
        coluNum+=(26*char[columnTitle[-2]])
        columnTitle = columnTitle[::-1]
        for i in range(2,len(columnTitle)):
            coluNum+=(26**i)*char[columnTitle[i]]
        return coluNum